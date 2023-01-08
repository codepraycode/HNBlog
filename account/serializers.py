from rest_framework import ModelSerializer
from .models import UserAccount

class UserAccountSerializer(ModelSerializer):
    """
        Serializer for user account object/instance
    """
    
    # validations and constraints already taken cared of by model
    
    class Meta:
        model = UserAccount
        fields = (
            'id',
            'username',
            'email',
            'is_verified',
        )