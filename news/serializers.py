from rest_framework.serializers import (
    ModelSerializer, 
    SerializerMethodField,
    IntegerField,
    ListField,
)
from datetime import datetime as dt
from .models import (
    ItemBaseModel, 
    StoryItemModel, 
    CommentItemModel
)

# For Incoming items
class ItemSerializer(ModelSerializer):
    
    """Serializer for incoming items
    """
    
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
            # 'deleted',
            # 'dead',
            'time',
            'kids',
        )
    
    def get_id(self, obj):
        if not isinstance(obj, self.Meta.model):
            return None
        
        hnid = obj.get('hnId')
        
        if hnid:
            return hnid
        
        return obj.get('id')

    def save(self, **kwargs):
        dtime = self.validated_data.get('time')
        
        if isinstance(dtime, int):
            self.validated_data['time'] = dt.fromtimestamp(dtime)

        dkids = self.validated_data.get('kids')
        
        if isinstance(dkids, list):
            self.validated_data['kids'] = str(dkids)
            
        return super().save(**kwargs)

# Outgoing items
class StoryItemSerializer(ItemSerializer):

    # validations and constraints already taken cared of by model
    
    kids = SerializerMethodField()
    
    class Meta:
        model = StoryItemModel
        fields = (
            *ItemSerializer.Meta.fields,
            'title',
            'url',
            'descendants',
            'score',
        )
    
    def get_kids(self, obj):

        ls = obj.kids.strip('][').replace(' ','').split(',') # remove spaces and split by comma
        # convert every item to integer
        if (len(ls) == 1) and not bool(ls[0]):
            return []
        
        return list(map(int, ls))



class CommentItemSerializer(ItemSerializer):

    # validations and constraints already taken cared of by model
    kids = SerializerMethodField()

    class Meta:
        model = CommentItemModel
        fields = (
            *ItemSerializer.Meta.fields,
            'text',
            'parent',
        )
    
    def get_kids(self, obj):

        ls = obj.kids.strip('][').replace(' ', '').split(
            ',')  # remove spaces and split by comma
        # convert every item to integer
        if (len(ls) == 1) and not bool(ls[0]):
            return []

        return list(map(int, ls))
