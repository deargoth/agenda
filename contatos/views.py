from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Contato
from django.views.generic.base import TemplateView


class Index(ListView):
    model = Contato
    template_name = 'contatos/index.html'
    context_object_name = 'contatos'
    
    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(contact_creator=self.request.user)
        
        return qs
    
class Detalhes(TemplateView):
    template_name = 'contatos/detalhes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['contato'] = Contato.objects.get(id=pk)

        return context

