from django.db import models
from django.utils.translation import gettext_lazy as _

"""
    This file holds base models for all apps in project
"""

class ItemBaseModel():
    """
        This is the Base model for all items
    """
    
    TYPE_CHOICES = [
        ("JOB", "job"),
        ("STORY", "story"),
        ("COMMENT", "comment"),
    ]
    
    by = models.CharField(
        _("Author"),
        max_length = 100, blank = True, null = True
    )
    deleted = models.BooleanField(
        _("Deleted"),
        default = False, null = True)
    dead = models.BooleanField(
        _("Dead"),
        default=False, null=True)
    _type = models.CharField(
        _("Type"),
        max_length = 10, 
        blank = False, 
        null = False,
        choices= TYPE_CHOICES
    )
    time = models.DateTimeField(blank = True, null = True)
    kids = models.TextField( # stores an array of integers as string
        _("Kids"),
        blank = True,
        null = True
        
        # converting snippet: list(map(int, arrr.strip('][').split(',')))
    )