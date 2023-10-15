from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from users.forms import *
from users.models import *


def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username = usuario, password = contra)
            
            if user is not None:
                login(request, user)
                
                return render(request, "SupermercadoApp/index.html", {"mensaje":f"Bienvenido {usuario}!"})
            else:
                
                return render(request, "SupermercadoApp/index.html", {"mensaje":"Error, datos incorrectos."})
            
        else:
            
            return render(request, "SupermercadoApp/index.html", {"mensaje": "Error en el formulario."})

    form = AuthenticationForm()
    
    return render(request, "SupermercadoApp/login.html", {"form": form})

def register(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)

        
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
        
    else:
        form = UserRegisterForm()
        
    return render(request, "SupermercadoApp/register.html", {"form":form})

@login_required
def profileEdit(request):
    
    usuario = request.user
    
    if request.method == "POST":
        
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            
            informacion = form.cleaned_data
            
            usuario.email = informacion["email"]
            if informacion["password1"]:
                usuario.set_password = informacion["password1"]
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            
            try:
                avatar = Avatar.objects.get(user=usuario)
            except Avatar.DoesNotExist:
                avatar = Avatar(user=usuario, imagen=informacion["avatar"])
                avatar.save()
            else:
                avatar.imagen = informacion["avatar"]
                avatar.save()

            return render(request, "AppCoder/index.html")

    
    else:
        form = UserEditForm(initial = {"email":usuario.email})
    
    return render(request, "SupermercadoApp/profile-edit.html", {"form": form, "user":usuario})
