from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Models
from .models import UserAccount

# Serializers
from .serializers import UserSerializer

# Create your views here.
class CreateUserAccountView(CreateAPIView):
    """
        View to create user account
        
        endpoints: 
            - /account (POST)
    """
    
    serializer_class = UserSerializer

class RetrieveUserAccountView(CreateAPIView):
    """
        View to authenticated user account
        
        endpoints: 
            - /account (GET)
    """
    
    permission_classes = (IsAuthenticated,)
    
    def get(self,request, *args,**kwargs):

        serialize = UserSerializer(instance=request.user)

        return Response(data=serialize.data)
    