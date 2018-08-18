from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    content = models.CharField(max_length=140)
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

class Comment(models.Model):
    content = models.CharField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_to = models.ForeignKey(Tweet, on_delete=models.CASCADE)

