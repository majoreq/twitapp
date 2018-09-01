"""twitterapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from messageapp.views import Hello, Login, Register, logoff, UserHomeScreen, AddTweet, HomeScreenAllTwet, AddComment, AllComments, addLike, AllMessages, SendMessage, ReadMessage, EditProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Hello.as_view(), name='main'),
    path('login', Login.as_view(), name='login'),
    path('register', Register.as_view(), name='register'),
    path('logout', logoff,name='logout'),
    path('home', UserHomeScreen.as_view(), name='home'),
    path('add_tweet', AddTweet.as_view(), name='add-tweet'),
    path('home_all', HomeScreenAllTwet.as_view(), name='home-all'),
    path('comment/<tweet_id>/add', AddComment.as_view(), name='add-comment'),
    path('comment/<tweet_id>', AllComments.as_view(), name='all-comments'),
    path('home/like/<tweet_id>', addLike, name='like'),
    path('messages', AllMessages.as_view(), name='messages'),
    path('send_message/<user_id>', SendMessage.as_view(), name='send-message'),
    path('message/<message_id>', ReadMessage.as_view(), name='read-message'),
    path('profile', EditProfile.as_view(), name='profile')
]
