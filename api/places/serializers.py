from rest_framework import serializers
from .models import Place
from comments.models import Comment
'''from comments.serializers import CommentPlaceListSerializer'''



class PlaceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Place
        fields = '__all__'
#Este serializador muestra todos los lugares
class GetPlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = [
            'id', 'name',
        ]

'''class PlaceListCommentSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Place
        fields = '__all__'   

    def get_comment(self, obj):
        selected_comment = Comment.objects.filter(place_id = obj.id)
        return CommentPlaceListSerializer(selected_comment, many=True).data'''
        