from __future__ import unicode_literals
import os

from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)
    poster = models.ImageField(upload_to='images/')
    info = models.CharField(max_length=512, default="Information Unavailable")
    category = models.CharField(max_length=32, default="Non-Categorized")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=60, unique=True)
    desc = models.TextField()
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=60, unique=True)
    post = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title
