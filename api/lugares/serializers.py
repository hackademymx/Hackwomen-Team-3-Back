from rest_framework import serializers
from .models import lugares


class lugaresSerializer(serializers.ModelSerializer): 

    class Meta:
        model = lugares
        fields = '_all_'
        