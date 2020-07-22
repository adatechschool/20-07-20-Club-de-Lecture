from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import UserSerializer, PostSerializer, MediaSerializer
from .models import User, Post, Media
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def all_users(request):
	if request.method =="GET":
		queryset = User.objects.all()

		user = request.query_params.get("user", None)
		if user is not None:
			queryset = queryset.filter(user__icontains=user)

		users_serializer = UserSerializer(queryset, many=True)
		return JsonResponse(users_serializer.data, safe=False)

	elif request.method == "POST":
		user_data = JSONParser().parse(request)
		user_serializer = UserSerializer(data=user_data)
		if user_serializer.is_valid():
			user_serializer.save()
			return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == "DELETE":
		count = User.objects.all().delete()
		return JsonResponse({"message": "{} Users were deleted succesfully!".format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# class Posts(viewsets.ModelViewSet):
# 	queryset = Post.objects.all().order_by("user_id")
# 	serializer_class = PostSerializer
#
# class Medias(viewsets.ModelViewSet):
# 	queryset = Media.objects.all().order_by("post_id")
# 	serializer_class = MediaSerializer
