from rest_framework.serializers import ModelSerializer, BooleanField
from .models import UserAccount

class UserAccountSerializer(ModelSerializer):
    """
        Serializer for user account object/instance
    """
    
    # validations and constraints already taken cared of by model
    
    is_verified = BooleanField(read_only=True)
    
    class Meta:
        model = UserAccount
        fields = (
            'id',
            'username',
            'email',
            'is_verified',
        )