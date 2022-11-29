from rest_framework import serializers
from .models import *
from pprint import pprint

class ServiceSerializer(serializer.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'description',)