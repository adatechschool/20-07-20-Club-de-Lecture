from django.db import models

# Create your models here.


# generate the table to store posts
class Post(models.Model):
    # user_id = models.ForeignKey("User", on_delete=models.CASCADE,) # add once the "User" table exists
    date = models.DateTimeField()
    description = models.CharField(max_length=500)

# generate the table to store the media that belong to certain posts
class Media(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    type = models.CharField(max_length=40)
