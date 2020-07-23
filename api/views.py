from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import UserSerializer, PostSerializer, MediaSerializer
from .models import User, Post, Media
from rest_framework.decorators import api_view


# for adding  and fetching users
@api_view(["GET", "POST"])
def users(request):
	if request.method =="GET":
		queryset = User.objects.all()

		# to search for specific users that contain the given characters
		user = request.query_params.get("user", None)
		if user is not None:
			queryset = queryset.filter(user__icontains=user)

		# returns all users that match the filter
		users_serializer = UserSerializer(queryset, many=True)
		return JsonResponse(users_serializer.data, safe=False)

	# adding a new user
	elif request.method == "POST":
		user_data = JSONParser().parse(request)
		user_serializer = UserSerializer(data=user_data)
		# verifies POST data
		if user_serializer.is_valid():
			user_serializer.save()
			return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
		# returns an error if NOT NULL or UNIQUE rules are not respected
		return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  for adding and fetching posts
@api_view(["GET", "POST", "PUT", "DELETE"])
def posts(request):
	if request.method == "GET":
		queryset = Post.objects.all()

		# to search for specific posts by users or content
		user_id = request.query_params.get("user_id", None)
		search = request.query_params.get("description", None)

		if user_id  is not None:
			queryset = queryset.filter(user_id__in=user_id)

		if search is not None:
			queryset = queryset.filter(description__icontains=search)

		# returns all posts that match the filter
		posts_serializer = PostSerializer(queryset, many=True)
		return JsonResponse(posts_serializer.data, safe=False)

	# adding a new post
	elif request.method == "POST":
		post_data = JSONParser().parse(request)
		post_serializer = PostSerializer(data=post_data)
		# verifies POST data
		if post_serializer.is_valid():
			post_serializer.save()
			return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# elif request.method == "PUT":


# class Medias(viewsets.ModelViewSet):
# 	queryset = Media.objects.all().order_by("post_id")
# 	serializer_class = MediaSerializer
