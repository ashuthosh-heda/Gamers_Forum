"""GamersForum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from gamers_forum.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/game/$', GameList.as_view()),
    url(r'^api/game/(?P<pk>[0-9]+)$', GameDetail.as_view()),
    url(r'^api/user/$', UserList.as_view()),
    url(r'^api/user/(?P<pk>[0-9]+)$', UserDetail.as_view()),
    url(r'^api/game/(?P<pk>[0-9]+)/topics/$', TopicList.as_view()),
    url(r'^api/game/(?P<id>[0-9]+)/topics/(?P<pk>[0-9]+)$', TopicDetail.as_view()),
    url(r'^api/game/(?P<id>[0-9]+)/topics/(?P<pk>[0-9]+)/posts/$', PostList.as_view()),
    url(r'^api/game/(?P<id1>[0-9]+)/topics/(?P<id2>[0-9]+)/posts/(?P<pk>[0-9]+)$', PostDetail.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
