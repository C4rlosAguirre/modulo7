from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from aplicacion.models import Cliente
from aplicacion.models import ClienteVip

from .models import Cliente
from .models import ClienteVip

            
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','apellido','edad','email','fecha_contratacion','clave','status')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmacion contraseña", widget=forms.PasswordInput)
    # date = forms.Charfield(widget=forms.DateField)

class Meta:
    model = User
    fields = ['username','email','password','password2']
    help_texts = {k:"" for k in fields}

    
#class LoginForm(forms.Form):
 #   nombre = forms.Charfield(widget=forms.TextInput)
  #  password = forms.Charfield(widget=forms.PasswordInput)

class ClienteVipForm(forms.ModelForm):
    class Meta:
        model = ClienteVip
        fields = ('nombre','apellido','edad','email','fecha_registro','fecha_nacimiento','clave','status')