from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models

class UserAccountManager(BaseUserManager):
    
    def validate_user_data(self, **user_data):
        """
            Receives user data, validates it and returns the data
            
            user_data includes:
            - username
            - email
            - password
            
            and they are all required.
        """
        username = data.get('username',None)
        email = data.get('email',None)
        password = data.get('password',None)
        
        if username is None:
            raise TypeError('username is required')
        if email is None:
            raise TypeError('email is required')
        if password is None:
            raise TypeError('password is required')
        
        return user_data
    
    def create_user(self, **data):#username, email, password
        
        user_data = self.validate_user_data(**data)
        
        user = self.model(
            username = user_data['username'],
            email = self.normalize_email(user_data['email'])
        )

        user.set_password(user_data['password'])
        user.is_active = True
        
        user.save()
        return user
    
    def create_superuser(self, **data):#username, email, password
        
        user_data = self.validate_user_data(**data)
        
        user = self.model(
            username = user_data['username'],
            email = self.normalize_email(user_data['email']),
            is_superuser = True,
            is_staff = True,
        )

        user.save()
        return user

# Create your models here.
class UserAccount(AbstractBaseUser, PermissionsMixin):
    """
        User Model
    """
    username = models.CharField(
        _("Username"),
        max_length = 255, 
        blank = False, 
        null = False,
        unique = True, # should be unique
    )
    email = models.EmailField(
        _("User email"),
        max_length = 255, 
        db_index = True,
        unique = True, # should be unique
    )
    password = models.CharField(
        _("User password"),
        max_length = 128,
    )
    
    # Meta data
    is_verified = models.BooleanField(default = True) # in case of email verification
    is_active = models.BooleanField(default = False) # if allowed to operate in app
    is_staff = models.BooleanField(default = False) # if app admin user
    date_joined = models.DateTimeField(auto_now_add=True,editable=True) # date account was created
    last_login = models.DateTimeField(_('last login'), blank=True, null=True) # last time account authenticated
    
    
    # Django Auth requirements
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=['email']
    
    # Custom model manager
    objects=UserAccountManager()
    
    # representation
    def __str__(self):
        return f"{self.username} - {self.email}"
    
    class Meta:
        db_table = "accounts_tb"
        verbose_name = "User account"
        verbose_name_plural = "Users account"
        