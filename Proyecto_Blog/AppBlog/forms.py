from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppBlog.models import AvatarImagen
from django.forms.fields import EmailField

class GamesForm(forms.Form):
    Titulo = forms.CharField(max_length = 200)
    Genero = forms.CharField(max_length = 100)
    Sintaxis = forms.CharField(max_length = 100000)
    
class MangaForm(forms.Form):
    Titulo = forms.CharField(max_length = 200)
    Genero = forms.CharField(max_length = 100)
    Sintaxis = forms.CharField(max_length = 100000)
    
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Ingresa Usuario')
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class meta: 
        model = User
        fields = ["username", "email", "password1", "password2"]
            
            
class EditarUsuario(UserCreationForm):
    username = forms.CharField(label='Ingresa Usuario')
    email = forms.EmailField()
    password1 = forms.CharField()

    class meta: 
        model = User
        fields = ["username", "email", "password1", "password2"]
    

    