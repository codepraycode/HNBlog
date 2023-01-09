from django.db import models
# from helpers.model import ItemBaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.
class StoryItemModel(models.Model):
    
    hnId = models.PositiveIntegerField(
        _("HackerNews Id"),
        blank=True, null=True
    )
    by = models.CharField(
        _("Author"),
        max_length=100, blank=True, null=True
    )
    deleted = models.BooleanField(
        _("Deleted"),
        default=False, null=True)
    dead = models.BooleanField(
        _("Dead"),
        default=False, null=True)

    time = models.DateTimeField(blank=True, null=True)
    kids = models.TextField(  # stores an array of integers as string
        _("Kids"),
        blank=True,
        null=True

        # converting snippet: list(map(int, arrr.strip('][').split(',')))
    )
    _type = models.CharField(
        _("Type"),
        max_length=10,
        blank=False,
        null=False,
        default = "story"
    )
    
    title = models.CharField(
        _("Title"),
        max_length = 225,
        blank = True,
        null = True
    )
    url = models.URLField(
        _("Url"),
        blank = True,
        null = True
    )
    descendants = models.PositiveIntegerField(
        _("Descendants"),
        blank = True,
        null = True
    )
    
    score = models.PositiveIntegerField(
        _("Score"),
        blank = True,
        null = True
    )
    
    author = property(lambda self: self.by or "Annonymous")

    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    class Meta:
        # db_table = "accounts_tb"
        verbose_name = "Story"
        verbose_name_plural = "Stories"
