from django.utils.translation import gettext_lazy as _
from django.db import models
import binascii
import os
from ..models import UserAccount

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