import django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone




class User(AbstractUser):
    pass

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.owner.username)


class Lk(models.Model):
    Users =models.ForeignKey(User, related_name="likeUser",on_delete=models.CASCADE)
    post =models.ForeignKey(Item, on_delete=models.CASCADE, related_name="like")









class Follower(models.Model):
    followed = models.ForeignKey(User, on_delete=models.CASCADE,related_name="followed")
    follower = models.ForeignKey(User, on_delete=models.CASCADE,related_name="follower")

    def __str__(self):
        return f"{self.followed} is following {self.follower}"











