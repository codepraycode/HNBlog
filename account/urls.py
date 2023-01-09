from django.urls import path

# Views
from .views import (
    CreateUserAccountView,
    RetrieveUserAccountView
)

from .auth.views import AuthenticateUserAccountView

urlpatterns = [
    path('', RetrieveUserAccountView.as_view(), name="account_get"),
    path('create/', CreateUserAccountView.as_view(), name="account_create"),
    path('signin/', AuthenticateUserAccountView.as_view(), name="account_signin")
]
