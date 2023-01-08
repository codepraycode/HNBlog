from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import parsers, renderers, serializers, exceptions
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import (
    ManualSchema,
    coreapi as coreapi_schema
)
from rest_framework.views import APIView

# models
from .models import (
    UserAccountAuthToken as UserAccountAuthTokenModel,
    UserAccount,
)

# Serializer
class UserAccountAuthSerialzier(serializers.Serializer):
    username = serializers.EmailField(
        label=_("Username"),
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:

            user = UserAccount.objects.authenticate(username = username, password = password)
            
            if not user:
                msg = _('Invalid username or password.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _("username and password is required.")
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

# Model
class AuthenticateUserAccountView(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser,
                      parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = UserAccountAuthSerialzier

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Enter your username",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Enter your password",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['association']
        token, created = UserAccountAuthTokenModel.objects.get_or_create(association=association)
        return Response({'token': token.key})


# View
class TokenAuthentication(BaseAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'Token'
    model = None

    def get_model(self):
        if self.model is not None:
            return self.model
        
        return UserAccountAuthTokenModel

    """
    A custom token model may be used, but must have the following properties.

    * key -- The string identifying the token
    * association -- The user to which the token belongs
    """

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Bad token.')
            raise exceptions.AuthenticationFailed(msg)
        
        user, _other = self.authenticate_credentials(token)
        request.user = user
        return (user, _other) # self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('association').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token'))

        if not token.association.is_active:
            raise exceptions.AuthenticationFailed(
                _('Account inactive or deleted.'))

        return (token.association, token)

    def authenticate_header(self, request):
        return self.keyword
