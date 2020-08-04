from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import UserSerializer, PostSerializer
from .models import User, Post
from rest_framework.decorators import api_view
from passlib.hash import argon2 as a2


# for adding  and fetching users
@api_view(["GET", "POST"])
def users(request):
	if request.method == "GET":
		queryset = User.objects.all()

		# to search for specific users that contain the given characters
		users = request.query_params.get("user_name", None)
		if users is not None:
			queryset = queryset.filter(user_name__icontains=users)
			print(queryset[0])

		# returns all users that match the filter
		users_serializer = UserSerializer(queryset, many=True)
		return JsonResponse(users_serializer.data, safe=False)

	# adding a new user
	elif request.method == "POST":
		users_data = JSONParser().parse(request)
		users_serializer = UserSerializer(data=users_data)
		# Encrypts password
		try:
			users_data["password"] = a2.using(rounds=5, salt_size=20, digest_size=20).hash(users_data["password"])
		except:
			pass
		# verifies POST data

		if users_serializer.is_valid():
			users_serializer.save()
			return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
		# returns an error if NOT NULL or UNIQUE rules are not respected
		return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def settings_password(request, user_name):
	# Check if selected user exists
	try:
		user = User.objects.get(user_name=user_name)
	except User.DoesNotExist:
		return JsonResponse({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

	if request.method == "PUT":
		user_data = JSONParser().parse(request)
		user_data["user_name"] = user_name
		# Encrypts password
		try:
			user_data["password"] = a2.using(rounds=5, salt_size=20, digest_size=20).hash(user_data["password"])
		except:
			pass

		user_serializer = UserSerializer(user, data=user_data)
		# verifies PUT data
		if user_serializer.is_valid():
			user_serializer.save()
			return JsonResponse(user_serializer.data)

	return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  for adding and fetching posts
@api_view(["GET", "POST"])
def posts(request):
	if request.method == "GET":
		queryset = Post.objects.all()

		# to search for specific posts by users or content
		user_id = request.query_params.get("user_id", None)
		user_name = request.query_params.get("user_name", None)
		search = request.query_params.get("description", None)

		if user_id  is not None:
			queryset = queryset.filter(user_id__in=user_id)

		if user_name is not None:
			queryset = queryset.filter(user_name=user_name)

		if search is not None:
			queryset = queryset.filter(description__icontains=search)

		# returns all posts that match the   filter
		posts_serializer = PostSerializer(queryset, many=True)
		return JsonResponse(posts_serializer.data, safe=False)

	# adding a new post
	elif request.method == "POST":
		posts_data = JSONParser().parse(request)
		posts_serializer = PostSerializer(data=posts_data)
		# verifies POST data
		if posts_serializer.is_valid():
			posts_serializer.save()
			return JsonResponse(posts_serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Access single posts for modification or maybe even display, idk
@api_view(["PUT"])
def modify_post(request, user_name, pk):
	# Check if selected post exists
	try:
		post = Post.objects.get(pk=pk, user_name=user_name)
	except Post.DoesNotExist:
		return JsonResponse({"message": "User or Post does not exist"}, status=status.HTTP_404_NOT_FOUND)

	if request.method == "PUT":
		post_data = JSONParser().parse(request)
		post_data["user_name"] = user_name

		post_serializer = PostSerializer(post, data=post_data)
		# verifies PUT data
		if post_serializer.is_valid():
			post_serializer.save()
			return JsonResponse(post_serializer.data)

		return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
