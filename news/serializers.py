from rest_framework.serializers import (
    ModelSerializer, 
    SerializerMethodField,
    IntegerField,
    ListField
)
from .models import ItemBaseModel, StoryItemModel, CommentItemModel

class ItemSerializer(ModelSerializer):
    
    id = SerializerMethodField()
    
    kids = ListField(
        child=IntegerField()
    )
    
    class Meta:
        model = ItemBaseModel
        fields = (
            'id',
            'type',
            'by',
            'deleted',
            'dead',
            'time',
            'kids',
        )
    
    def get_id(self, obj):
        if obj.hnId:
            return obj.hnId
        
        return obj.id

    def save(self, **kwargs):
        print(self.validated_data)
        # return super().save(**kwargs)

class StoryItemSerializer(ItemSerializer):

    # validations and constraints already taken cared of by model
    
    class Meta:
        model = StoryItemModel
        fields = (
            *ItemSerializer.Meta.fields,
            'title',
            'url',
            'descendants',
            'score',
        )


class CommentItemSerializer(ItemSerializer):

    # validations and constraints already taken cared of by model

    class Meta:
        model = CommentItemModel
        fields = (
            *ItemSerializer.Meta.fields,
            'text',
            'parent',
        )
