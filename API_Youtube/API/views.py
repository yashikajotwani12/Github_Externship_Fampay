from django.shortcuts import render
from django.http import HttpResponse

from .Test_Youtube_api import getnewposts
from .models import Videos
from .serializers import VideosSerializer

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# Create your views here.

def fetch_new_posts(request):
    try:
        getnewposts()
        return HttpResponse("New videos have been fetched! Refresh Localhost to view added videos")
    except:
        return HttpResponse("Some error encountered")

class VideoList(generics.ListAPIView):
    queryset = Videos.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
   
    # Adding the search and filter fields
    search_fields = ['title']
    filter_fields = ['channelTitle']

    # For sorting the videos' data in reverse chronological order by default
    ordering = ['-publishingDateTime']
    serializer_class = VideosSerializer
    pagination_class = PageNumberPagination