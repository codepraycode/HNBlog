from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import UserAccount
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(UserAccount)
class UserAccountAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'is_staff',
    )
    
    search_fields = (
        'username',
        'email'
    )
    
    fieldsets = (
        (_("User Info"), {
            "fields": (
                'username',
                'email',
                'password'
            ),
        }),
    )
    