from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña: ", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repite tu contraseña: ", widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, label="Nombre")
    last_name = forms.CharField(max_length=30, label="Apellido")
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]
        
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar E-mail", required=False)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Repite la contraseña", widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(max_length=30, label="Nombre", required=False)
    last_name = forms.CharField(max_length=30, label="Apellido", required=False)   
    
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}

