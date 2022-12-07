from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Service)
admin.site.register(Listing)
admin.site.register(Review)
admin.site.register(ListingService)
admin.site.register(UserListing)
admin.site.register(UserImage)
admin.site.register(Image)
admin.site.register(UserReview)
