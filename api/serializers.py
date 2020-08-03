from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_name", "email", "password", "avatar")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "user_name", "creation_date", "description")
