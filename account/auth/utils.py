from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from .model import UserAccountAuthToken as UserAccountAuthTokenModel

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
