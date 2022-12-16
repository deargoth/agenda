from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from contatos.models import Contato


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'
        
class CreateContact(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'