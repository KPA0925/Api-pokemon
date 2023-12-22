from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuarios


class RegistroUsuarioForm(UserCreationForm):
    correo_usuario = forms.EmailField(label="Ingrese su correo")
    nombre_usuario = forms.CharField(label="Ingrese su nombre de usuario")
    password1 = forms.CharField(label="Ingrese una contraseña", widget=forms.PasswordInput, help_text='')
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, help_text='')
    class Meta:
        model = Usuarios
        fields = ['correo_usuario', 'nombre_usuario', 'password1', 'password2']

class InicioSesionForm(AuthenticationForm):
    class Meta:
        model = Usuarios
        fields = ['correo_usuario', 'password_usuario']