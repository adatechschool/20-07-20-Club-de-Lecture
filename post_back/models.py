from django.db import models

# Create your models here.


class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.CharField(max_length=500)
