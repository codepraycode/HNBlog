from helpers.models import BaseModel
from django.utils.translation import gettext_lazy as _


class UserAccountManager():
    pass

# Create your models here.
class UserAccount(BaseModel):
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
    is_active = models.BooleanField(default = True) # if allowed to operate in app
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
        