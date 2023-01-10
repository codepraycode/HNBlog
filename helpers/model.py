from django.db import models
from django.utils.translation import gettext_lazy as _

"""
    This file holds base models for all apps in project
"""

class AbstractItemBaseModel():
    """
        This is the Base model for all items
    """
    
    
    class Types(models.TextChoices):
        JOB = "JOB", "job"
        STORY = "STORY", "story"
        COMMENT = "COMMENT", "comment"
    
    hnId = models.PositiveIntegerField(
        _("HackerNews Id"),
        blank=True, null=True
    )
    
    type = models.CharField(
        _("Type"),
        max_length = 10, 
        blank = False, 
        null = False,
        choices = Types.choices,
        default = Types.STORY
    )
    
    by = models.CharField(
        _("Author"),
        max_length=100, blank=True, null=True
    )

    deleted = models.BooleanField(
        _("Deleted"),
        default=False,
        null=True
    )

    dead = models.BooleanField(
        _("Dead"),
        default=False, null=True
    )
    
    time = models.DateTimeField(
        blank = True, 
        null = True
    )
    
    kids = models.TextField( # stores an array of integers as string
        _("Kids"),
        blank = True,
        null = True
        
        # converting snippet: list(map(int, arrr.strip('][').split(',')))
    )
    
    # For stories
    title = models.CharField(
        _("Title"),
        max_length=225,
        blank=True,
        null=True
    )
    
    url = models.URLField(
        _("Url"),
        blank=True,
        null=True
    )
    
    descendants = models.PositiveIntegerField(
        _("Descendants"),
        blank=True,
        null=True
    )
    
    score = models.PositiveIntegerField(
        _("Score"),
        blank=True,
        null=True
    )

    
    # For comments
    text = models.CharField(
        _("Text"),
        max_length=225,
        blank=True,
        null=True
    )

    parent = models.PositiveIntegerField(
        _("Parent"),
        blank=True,
        null=True
    )
    
    author = property(lambda self: self.by or "Annonymous")
    
    class Meta:
        abstract = True