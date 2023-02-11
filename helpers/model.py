from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.core.validators import validate_comma_separated_integer_list
from django.db.models.fields import DateTimeField
from datetime import datetime as dt

"""
    This file holds base models for all apps in project
"""
      

class AbstractItemBaseModelMethods():
    """Custom field methods for model
    """
    
    # # Setter and getter for kids field
    # def kids_setter(self, value):
    #     # convert a list of integers to string
    #     # converting snippet: list(map(int, arrr.strip('][').split(',')))
        
    #     print("Running kids_setter...")
    #     # value is a string of list
    #     ls = value.strip('][').replace(' ','').split(',') # remove spaces and split by comma
    #     # convert every item to integer
    #     return list(map(int, ls))
    
    # def kids_getter(self, value):
    #     # convert string of a list of integers to actual list of integers
    #     print("Running kids_getter...")
    #     # value is a list of integers
    #     ls = value.strip('][').replace(' ','').split(',') # remove spaces and split by comma
    #     # convert every item to integer
    #     if (len(ls) == 1) and not bool(ls[0]):
    #         return []
        
    #     return list(map(int, ls))
    
    # # Setter and getter for time field
    # def get_time(self, value):
    #     # convert a timestamp to a datetime instance
        
    #     # incoming value will be a timestamp
    #     tm = dt.fromtimestamp(value)
        
    #     return tm
    
    
    
    def time_getter(self, value):
        # convert a timestamp to a datetime instance
        # incoming value will be a datetime instance
        if isinstance(value, dt):
            return value.timestamp()
        
        return value
    

class AbstractItemBaseModel(models.Model):
    """
        This is the Base model for all items
    """
    
    
    class Types(models.TextChoices):
        JOB = 'job', "JOB"
        STORY = 'story', "STORY"
        COMMENT = 'comment', "COMMENT"
    
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
    
    time = DateTimeField(
        blank = True, 
        null = True,
    )
    
    kids = models.TextField( # stores an array of integers as string
        _("Kids"),
        blank = True,
        null = True,
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