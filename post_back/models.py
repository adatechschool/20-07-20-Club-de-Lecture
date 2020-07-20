from django.db import models

# Create your models here.


class Post(models.Model):
    user_id = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length=500)
