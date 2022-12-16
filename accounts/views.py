from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm, LoginForm, CreateContact
from contatos.models import Contato
from django.contrib.auth.mixins import LoginRequiredMixin


class Register(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = '/accounts/login/'


class Login(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    next_page = '/'
    
class Logout(LogoutView):
    next_page = '/'

class Dashboard(LoginRequiredMixin, CreateView):
    model = Contato
    form_class = CreateContact
    login_url = '/accounts/login'
    template_name = 'accounts/dashboard.html'

