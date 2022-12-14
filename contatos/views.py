from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Contato


class Index(ListView):
    model = Contato
    template_name = 'contatos/index.html'
    context_object_name = 'contato'
    