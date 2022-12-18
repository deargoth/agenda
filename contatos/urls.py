from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="agenda_index"), 
    path('detalhes/<int:pk>', views.Detalhes.as_view(), name="detalhes"),
]