from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Contato


class Index(ListView):
    model = Contato
    template_name = 'contatos/index.html'
    context_object_name = 'contatos'
    
    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(contact_creator=self.request.user)
        
        return qs