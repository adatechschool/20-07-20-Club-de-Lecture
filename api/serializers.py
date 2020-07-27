from rest_framework import serializers
from .models import User, Post, Media

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_name", "email", "password", "avatar")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("user", "creation_date", "description")

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ("post", "content", "type")
