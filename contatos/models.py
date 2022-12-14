from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    name_cat = models.CharField(max_length=64)

    def __str__(self):
        return self.name_cat


class Contato(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64, blank=True)
    phone = models.CharField(max_length=64)
    email = models.EmailField(blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    show = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to='')

    def __str__(self):
        return self.name