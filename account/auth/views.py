from rest_framework import parsers, renderers
from rest_framework.views import APIView

from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import (
    ManualSchema,
    coreapi as coreapi_schema
)
# from rest_framework.views import APIView

# models
from .model import UserAccountAuthToken as UserAccountAuthTokenModel

# Serializer
from .serializer import UserAccountAuthSerialzier
    
# Authentication
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
        user = serializer.validated_data['user']
        token, created = UserAccountAuthTokenModel.objects.get_or_create(association=user)
        return Response({'token': token.key})
