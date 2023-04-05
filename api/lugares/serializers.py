from rest_framework import serializers
from .models import lugar


class lugarSerializer(serializers.ModelSerializer): 

    class Meta:
        model = lugar
        fields = '_all_'
        