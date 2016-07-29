from gamers_forum.models import *
from django.contrib.auth.models import User
from gamers_forum.serializers import *
from rest_framework import generics, permissions


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class TopicList(generics.ListCreateAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        game_id = int(self.kwargs['pk'])
        return Topic.objects.all().filter(game_id=game_id)


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        topic_id = int(self.kwargs['pk'])
        return Topic.objects.all().filter(id=topic_id)


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        topic_id = int(self.kwargs['pk'])
        return Post.objects.all().filter(topic_id=topic_id)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        post_id = int(self.kwargs['pk'])
        return Post.objects.all().filter(id=post_id)

