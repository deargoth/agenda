from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from contatos.models import Contato
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        
    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error(error)
                print(error)
                
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'
        
class CreateContact(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        exclude = ('contact_creator', 'creation_date', )