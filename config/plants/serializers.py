from rest_framework import serializers
from .models import *
from pprint import pprint

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("__all__")
