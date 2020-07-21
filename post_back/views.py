# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PostSerializer, MediaSerializer
from .models import Post, Media

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('description')
	serializers_class = PostSerializer

class MediaViewSet(viewsets.ModelViewSet):
	queryset = Media.objects.all().order_by('post_id')
	serializers_class = MediaSerializer
