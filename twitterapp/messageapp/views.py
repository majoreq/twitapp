from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import Tweet
from .forms import LoginForm, RegisterForm, AddTweetForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class Hello(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'main.html', {'form':form})

    def post(self, request):
        form = LoginForm()
        return render(request, 'main.html', {'form': form})


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error = "Wrong username or password"
                return render(request, 'login.html', {'form': form, 'error':error})
        return HttpResponse("Not working")


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                return redirect('main')
            else:
                HttpResponse("Password didnt match")
        HttpResponse("Not working")


def logoff(request):
    logout(request)
    return redirect('main')

class UserHomeScreen(View):
    def get(self, request):
        user = User.objects.get(id = request.user.id)
        tweets = Tweet.objects.filter(author=user)
        return render(request, 'home.html', {'tweets':tweets})

class AddTweet(View):
    def get(self, request):
        form = AddTweetForm()
        return render(request,'newTweet.html', {'form':form})

    def post(self, request):
        form = AddTweetForm(request.POST)
        if form.is_valid():
            Tweet.objects.create(content=form.cleaned_data['content'],
                                 author=request.user)
            return redirect('home')
        error = "coś poszło nie tak"
        return render(request,'newTweet.html', {'form':form, 'error':error})

