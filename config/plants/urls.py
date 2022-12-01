from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithUserNameView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]