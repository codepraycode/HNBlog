from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
import binascii
import os

class UserAccountManager(BaseUserManager):
    
    def validate_user_data(self, **data):
        """
            Receives user data, validates it and returns the data
            
            data includes:
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
        
        return data
    
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
        )
        
        user.set_password(user_data['password'])
        user.is_active = True,
        user.is_superuser = True,
        user.is_staff = True,

        user.save()
        return user
    
    def authenticate(self, **data):

        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise TypeError('username is required')

        if password is None:
            raise TypeError('password is required')

        try:            
            user = self.model.objects.get(
                username = username
            )
        except self.model.DoesNotExist:
            return None

        valid_password = user.check_password(password)
        

        if not valid_password:
            return None

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



# For authentication

class UserAccountAuthToken(models.Model):
    """
    The default authorization token for UserAccount model.
    """
    key = models.CharField(
        _("Key"),
        max_length = 40, 
        primary_key = True
    ) # authentication token

    association = models.OneToOneField(
        UserAccount, 
        related_name = 'auth_token',
        on_delete = models.CASCADE, 
        verbose_name = _("User account")
    )
    created = models.DateTimeField(
        _("Created"),
        auto_now_add = True
    )

    class Meta:
        # abstract = 'api.authentication' not in settings.INSTALLED_APPS
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key