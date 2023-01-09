from rest_framework.serializers import ModelSerializer, BooleanField, CharField
from .models import UserAccount

class UserAccountSerializer(ModelSerializer):
    """
        Serializer for user account object/instance
    """
    
    # validations and constraints already taken cared of by model
    
    is_verified = BooleanField(read_only=True)
    password = CharField(write_only = True)
    class Meta:
        model = UserAccount
        fields = (
            'id',
            'username',
            'email',
            'is_verified',
            'password',
        )
        
    def create(self, validated_data):
        # return super().create(validated_data)
        
        return self.Meta.model.objects.create_user(**validated_data)