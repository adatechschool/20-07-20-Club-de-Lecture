from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^api/users$', views.users),
	url(r'^api/posts$', views.posts),
	# url(r'^api/medias$', views.Medias),
]
