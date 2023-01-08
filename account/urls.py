from django.urls import path

# Views
from .views import (
    CreateUserAccountView,
    GetUserAccountView,
)


urlpatterns = [
    path('', GetUserAccountView.as_view(), name="account:get")
    path('create/', CreateUserAccountView.as_view(), name="account:create")
]
