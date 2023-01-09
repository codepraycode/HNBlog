from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from ..models import UserAccount

class UserAccountAuthSerialzier(serializers.Serializer):
    username = serializers.CharField(
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
            
            try:

                user = UserAccount.objects.authenticate(
                    username = username,
                    password = password
                )
            
            except Exception as err:
                # msg = _('Invalid username or password.')
                raise serializers.ValidationError(err, code='authorization')
        else:
            msg = _("username and password is required.")
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
