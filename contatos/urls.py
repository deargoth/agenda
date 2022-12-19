from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="agenda_index"), 
    path('detalhes/<int:pk>', views.Detalhes.as_view(), name="detalhes"),
    path('edit/<int:pk>', views.Editing.as_view(), name="edit"),
    path('busca/', views.Busca.as_view(), name="busca"),
]