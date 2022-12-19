from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Contato
from .forms import EditingForm


class Index(ListView):
    model = Contato
    template_name = 'contatos/index.html'
    context_object_name = 'contatos'
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('category')
        qs = qs.order_by('-id').filter(show=True)

        if self.request.user.is_authenticated:
            qs = qs.filter(contact_creator=self.request.user)

        return qs


class Busca(Index):
    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        campos = Concat('name', Value(' '), 'surname')
        
        qs = qs.annotate(
            fullname=campos
        ).filter(
            Q(fullname__icontains=termo) |
            Q(phone__icontains=termo)
        )
        
        return qs


class Detalhes(TemplateView):
    template_name = 'contatos/detalhes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['contato'] = Contato.objects.get(id=pk)

        return context


class Editing(UpdateView):
    model = Contato
    template_name = 'contatos/editing.html'
    form_class = EditingForm
    success_url = '/'
