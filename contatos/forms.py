from django import forms
from .models import Contato

class EditingForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        exclude = ('contact_creator', 'creation_date', )