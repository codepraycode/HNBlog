from helpers.models import BaseModel
from django.utils.translation import gettext_lazy as _

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