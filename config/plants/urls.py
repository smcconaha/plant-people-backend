from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register(r'services', ServiceViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'images', ImageViewSet)
router.register(r'all', AllListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('edit/listing/<int:pk>/', ListingDetail.as_view()),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithUserNameView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('search/', ListingList.as_view()),
    # path('search/<int:pk>/', PkList.as_view())
    path('search/', SearchDetail.as_view(), name='detailsearch') #dont need to define data in slug as normal
]