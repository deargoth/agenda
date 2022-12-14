from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm


class Login(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


class Register(CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = RegisterForm
