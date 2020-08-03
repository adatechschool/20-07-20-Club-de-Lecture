from django.db import models

# Create your models here.

# generate the table to store user account data
class User(models.Model):
    user_name = models.CharField(max_length=20, blank=False, unique=True)
    email = models.EmailField(max_length=40, blank=False,  unique=True)
    password = models.CharField(max_length=10000, blank=False)
    avatar = models.CharField(max_length=200, blank=True)

    def save(self, method=None, *args, **kwargs):
        print(method)
        if method == "PUT":
            if User.objects.get(user_name=user_name):
                print("lol")
            print("hey")
            # try:
            #     existing_user = User.objects.get(user_name=user_name)
            # except:
            #     pass
        return

# generate the table to store posts
class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    description = models.CharField(max_length=500, blank=False)

# generate the table to store the media that belong to certain posts
class Media(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    content = models.CharField(max_length=200, blank=False)
    type = models.CharField(max_length=40, blank=False)
