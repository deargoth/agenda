from django.contrib import admin
from .models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'category', 'phone', 'creation_date', 'show')
    list_editable = ('phone', 'show')
    list_display_links = ('id', 'name', 'surname')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat')
    list_display_links = ('id', 'name_cat')


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria, CategoriaAdmin)