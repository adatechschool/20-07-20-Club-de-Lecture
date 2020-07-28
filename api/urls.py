from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^users$", views.users),
	url(r"^posts$", views.posts),
	url(r"^posts/(?P<pk>[0-9]+)$", views.post),
	# url(r"^api/medias$", views.Medias),
	url(r"^login$", views.login),
]
