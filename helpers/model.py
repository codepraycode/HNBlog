from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.core.validators import validate_comma_separated_integer_list
from django.db.models.fields import DateTimeField

"""
    This file holds base models for all apps in project
"""

class UCDateTimeField(DateTimeField):

    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            value = datetime.datetime.now()
            setattr(model_instance, self.attname, value)
            return value
        else:
            value = getattr(model_instance, self.attname)
            if not isinstance(value, datetime):
                # assume that the value is a timestamp if it is not a datetime
                value = datetime.fromtimestamp(int(value))
                # an exception might be better than an assumption
                setattr(model_instance, self.attname, value)
            return super(UCDateTimeField, self).pre_save(model_instance, add)
        

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
    
    time = UCDateTimeField(
        blank = True, 
        null = True
    )
    
    kids = models.TextField( # stores an array of integers as string
        _("Kids"),
        blank = True,
        null = True,
        validators = (validate_comma_separated_integer_list,)
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