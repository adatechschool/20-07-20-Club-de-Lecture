from django.db import models

# Create your models here.

# generate the table to store user account data
class User(models.Model):
    user = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=30, blank=False)
    password = models.CharField(max_length=10000, blank=False)
    avatar = models.CharField(max_length=200)

# generate the table to store posts
class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE) # add once the "User" table exists
    date = models.DateTimeField()
    description = models.CharField(max_length=500, blank=False)

# generate the table to store the media that belong to certain posts
class Media(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    content = models.CharField(max_length=200, blank=False)
    type = models.CharField(max_length=40, blank=False)
