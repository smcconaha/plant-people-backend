from django.shortcuts import render
from django.http.response import Http404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, permissions, generics, filters
from rest_framework.decorators import action, api_view
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser

# Create your views here.

# class ListingDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Listing.objects.get(pk=pk)
#         except Listing.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         listing = self.get_object(pk)
#         serializer = ListingSerializer(listing)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         listing = self.get_object(pk)
#         serializer = ListingSerializer(listing, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         listing = self.get_object(pk)
#         listing.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ListingList(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = ListingSerializer 

#     #custom queryset, overriding basic functionality
#     def get_queryset(self):
#         return Listing.objects.filter(city="Georgetown")
#     #only post that are in Georgetown

# class PkList(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = ListingSerializer 
    # def get_queryset(self):
    #     """
    #     Filtering against the URL (ID)
    #     Get post based on title / string
    #     """
    #     slug = self.kwargs['pk']
    #     print(slug)
    #     return Listing.objects.filter(id=slug)

class SearchDetail(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = [filters.SearchFilter] #extends filter with searchfilter, use end point and ? to take in diff params and run filter
    search_fields = ['=zip_code']

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class AllListingViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = ViewAllListSerializer

class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ObtainTokenPairWithUserNameView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = () #added

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

