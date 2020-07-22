from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^api/users$', views.all_users),
	# url(r'^api/posts$', views.Posts),
	# url(r'^api/medias$', views.Medias),
]
