from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InvestigadorxsFormulario (forms.Form):
    Nombre = forms.CharField(max_length=50)
    Apellido = forms.CharField(max_length=50)
    Titulo = forms.CharField(max_length=50)
    Pertenencia_institucional = forms.CharField(max_length=50)
    Edad = forms.IntegerField()
    email = forms.EmailField(max_length = 60) 

class PublicacionesFormulario (forms.Form):
    Título = forms.CharField(max_length=100)
    Autorxs = forms.CharField(max_length=50)
    Pertenencia_institucional_de_autorxs = forms.CharField(max_length=50)
    url_de_la_publicacion = forms.URLField(max_length = 200)


class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

class Meta:
   model = User
   fields = ['username', 'email', 'password1', 'password2']
   help_texts={k:"" for k in fields}

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
  first_name = forms.CharField(label='Modificar el nombre')
  last_name = forms.CharField(label='Modificar el apellido')
  email = forms.EmailField(required=True)
  password1 = forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput, required=False)
  password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput, required=False)


  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']
    help_texts={k:"" for k in fields}