from django.urls import path

# Views
from .views import (
    CreateUserAccountView,
    GetUserAccountView,
)

from .authentication import TokenAuthentication

urlpatterns = [
    path('', GetUserAccountView.as_view(), name="account:get")
    path('create/', CreateUserAccountView.as_view(), name="account:create")
    path('signin/', TokenAuthentication.as_view(), name="account:signin")
]
