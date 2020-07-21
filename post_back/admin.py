from django.contrib import admin

# Register your models here.

from .models import Media, Post


admin.site.register(Post)
admin.site.register(Media)
