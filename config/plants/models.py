from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class Service(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    service_type = models.CharField(max_length=50, null=False, blank=True, unique=False)
    description = models.CharField(max_length=255, null=True, blank=True, unique=False)
    
    # def __str__(self):
    #     return self.name

class Listing(models.Model):
    Invisible = 0
    Draft = 1
    Published = 2
    Promoted = 3
    STATUS_CHOICES = [
        (Invisible, 0),
        (Draft, 1),
        (Published, 2),
        (Promoted, 3)
    ]
    heading = models.CharField(max_length=50, default="Certified Caregiver", null=False, blank=False, unique=False)
    body = models.CharField(max_length=1000, null=False, blank=False, unique=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    service = models.ManyToManyField(Service, through='ListingService', related_name="listings")
    address_line_one = models.CharField(max_length=100, null=True, blank=False)
    address_line_two = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=85, null=True, blank=False)
    state = models.CharField(max_length=85, null=True, blank=False)
    zip_code = models.PositiveIntegerField(null=True, validators=[MinValueValidator(501), MaxValueValidator(99950)])
    country = models.CharField(max_length=60, null=False, default="US", blank=False)
    status = models.PositiveSmallIntegerField(null=False, choices=STATUS_CHOICES, validators=[MinValueValidator(0), MaxValueValidator(4)])

class Review(models.Model):
    rating = models.PositiveSmallIntegerField(null=False, default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=50, null=False, blank=False, unique=True)
    body = models.CharField(max_length=1000, null=False, blank=False, unique=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.title

class Image(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False, unique=True)
    profile_image = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)

class ListingService(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)

    class Meta:
        unique_together = (
            ['listing', 'service']
        )

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)
    listings = models.ManyToManyField(Listing, through='UserListing', related_name="userlist_list")
    images = models.ManyToManyField(Image, through='UserImage', related_name="userimg_list")
    reviews = models.ManyToManyField(Review, through='UserReview', related_name="userrev_list")


    extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserListing(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    listing = models.ForeignKey(Listing, on_delete=models.PROTECT)

    # def __str__(self):
    #     return self.user

class UserImage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


class UserReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    review= models.ForeignKey(Review, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user