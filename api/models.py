from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # spouse_name = models.CharField(blank=True, max_length=100)
    # date_of_birth = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.email


# generate the table to store user account data
class User(models.Model):
    avatar = models.CharField(max_length=200, blank=True)

# generate the table to store posts
class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE) # add once the "User" table exists
    creation_date = models.DateTimeField()
    description = models.CharField(max_length=500, blank=False)

# generate the table to store the media that belong to certain posts
class Media(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    content = models.CharField(max_length=200, blank=False)
    type = models.CharField(max_length=40, blank=False)
