from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from aplicacion.models import Cliente, ClienteVip, Contacto, Proveedor, Tienda, Subfamilia

from .models import Cliente, Contacto, Tienda, Subfamilia, ClienteVip, Proveedor
            
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

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ('nombre','apellido','correo','comentario')

class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = Proveedor
        fields = ('nombre','nombrefantasia','direccion','email','familia','tienda')

class TiendaForm(forms.ModelForm):

    class Meta:
        model = Tienda
        fields = ('nombre','direccion','email')

class Subfamilia(forms.ModelForm):

    class Meta:
        model = Subfamilia
        fields = ('nombre','proveedor','tienda')               
    




