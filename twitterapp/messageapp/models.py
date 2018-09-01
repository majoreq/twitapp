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

class Message(models.Model):
    from_who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_who')
    to_who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_who')
    content = models.CharField(max_length=256)
    readed = models.BooleanField(default=False)

