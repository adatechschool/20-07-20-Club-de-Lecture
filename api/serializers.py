from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_name", "email", "password", "creation_date", "avatar")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "user_name", "creation_date", "description")

class PasswordChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_name", "old_password", "new_password", "new_password_repeat")
