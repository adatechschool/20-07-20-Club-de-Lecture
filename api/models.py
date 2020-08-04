from django.db import models

# Create your models here.

# generate the table to store user account data
class User(models.Model):
    user_name = models.CharField(max_length=20, blank=False, unique=True)
    email = models.EmailField(max_length=40, blank=False,  unique=True)
    password = models.CharField(max_length=10000, blank=False)
    creation_date = models.DateTimeField(auto_now=True, editable=False)
    avatar = models.URLField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        super().save()
        return

# generate the table to store posts
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey("User", to_field="user_name", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True, editable=False)
    description = models.CharField(max_length=500, blank=False)

    def save(self, *args, **kwargs):
        super().save()
        return
