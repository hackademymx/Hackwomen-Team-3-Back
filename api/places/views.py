#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Place
from .serializers import PlaceSerializer

# Create your views here.

class PlaceAPIView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def get(self, request): 
    
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request): 
        serializer = PlaceSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class PlaceAPIUpdateDeleteView(APIView):
    
    def patch(self, request, id):
        place = Place.objects.filter(id=id).first()
        if place is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PlaceSerializer(place, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_0K)
    
    def delete(self, request, id):
        place = Place.objects.filter(id=id).first()
        if place is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        place.delete()
        return Response({'message': 'lugar eliminado satisfactoriamente'}, status=status.HTTP_200_OK)
        

