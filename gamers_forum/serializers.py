from gamers_forum.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

    def create(self, attrs):
        user = super(UserSerializer, self).create(attrs)
        user.set_password(attrs['password'])
        user.save()
        return user
