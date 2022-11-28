from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)

    def __str__(self):
        return self.username

class Service(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class Listing(models.Model):
    body = models.CharField(max_length=1000, null=False, blank=False, unique=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    service = models.ManyToManyField(Service, through='ListingService', related_name="listing_list")
    
    def __str__(self):
        return self.name

class ListingService(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)

    class Meta:
        unique_together = (
            ['listing', 'service']
        )
