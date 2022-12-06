from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from .fields import *
from pprint import pprint

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("__all__")

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "rating", "title", "body", "created_date")

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "title", "profile_image")

class ListingSerializer(serializers.ModelSerializer):
    service = ServiceListingField(many=True, queryset=Service.objects.all(), required=True)
    class Meta:
        model = Listing
        fields = ["id", "body", "service", "address_line_one", "address_line_two", "city", "state", "zip_code", "country", "status"]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom birthday
        token['username'] = user.username
        return token

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    birthday = serializers.DateField(required=False)
    password = serializers.CharField(min_length=8, write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'birthday')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance    