from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm
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
                return redirect('main')
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