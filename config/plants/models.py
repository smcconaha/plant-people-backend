from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)

    def __str__(self):
        return self.username

    extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class Service(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    service_type = models.CharField(max_length=50, null=False, blank=True, unique=False)
    description = models.CharField(max_length=255, null=True, blank=True, unique=False)
    
    def __str__(self):
        return self.name

class Listing(models.Model):
    body = models.CharField(max_length=1000, null=False, blank=False, unique=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    service = models.ManyToManyField(Service, through='ListingService', related_name="listing_list")
    status = models.PositiveSmallIntegerField(null=False, default=1, validators=[MinValueValidator(0), MaxValueValidator(4)])
    
    def __str__(self):
        return self.name

class ListingService(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)

    class Meta:
        unique_together = (
            ['listing', 'service']
        )

class UserListing(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    listing = models.ForeignKey(Listing, on_delete=models.PROTECT)