from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^users$", views.users),
	url(r"^posts$", views.posts),
	url(r"^posts/(?P<user_name>.+)/(?P<pk>[0-9]+)$", views.modify_post),
	url(r"^(?P<user_name>.+)/settings/password$", views.settings_password),
	# url(r"^api/medias$", views.Medias),
	]
