from django.db import models
from helpers.model import AbstractItemBaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ItemBaseModel(AbstractItemBaseModel):

    class Meta:
        db_table = "items_tb"

class StoryItemManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(type = ItemBaseModel.Types.STORY)
class StoryItemModel(ItemBaseModel):
    
    class Meta:
        proxy = True
        verbose_name = "Story"
        verbose_name_plural = "Stories"
    
    objects = StoryItemManager()
    
    def save(self, *args, **kwargs):
        self.type = ItemBaseModel.Types.STORY
        
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"stroy: {self.title} - {self.author}"



class CommentItemManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(type = ItemBaseModel.Types.COMMENT)


class CommentItemModel(ItemBaseModel):
    
    objects = CommentItemManager()
    
    def save(self, *args, **kwargs):
        self.type = ItemBaseModel.Types.COMMENT

        return super().save(self, *args, **kwargs)

    def __str__(self):
        return f"comment: {self.text[:20]}{(len(self.text) > 20 ) and '...'}"

    class Meta(ItemBaseModel.Meta):
        proxy = True
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
