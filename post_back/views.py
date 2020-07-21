from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PostSerializer, MediaSerializer
from .models import Post, Media

# Create your views here.
