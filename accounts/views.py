from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm


class Register(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = '/accounts/login/'


class Login(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    next_page = '/'


