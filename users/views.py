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
                
                return render(request, "SupermercadoApp/index.html")
                
        else:
            return render(request, "SupermercadoApp/index.html", {"form":form, "mensaje":"Datos incorrectos. Revisa el usuario y/o contraseña."})

    form = AuthenticationForm()
    
    return render(request, "users/login.html", {"form": form})

def register(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)

        
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
        
    else:
        form = UserRegisterForm()
        
    return render(request, "users/register.html", {"form":form})

@login_required
def profileEdit(request):
    
    usuario = request.user
    
    if request.method == "POST":
        
        form = UserEditForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            informacion = form.cleaned_data
            usuario.email = informacion["email"]
            
            if informacion["password1"]:
                usuario.set_password = informacion["password1"]
            if informacion["last_name"]:
                usuario.last_name = informacion['last_name']
            if informacion["last_name"]:
                usuario.first_name = informacion['first_name']
            usuario.save()
            
            try:
                avatar = Avatar.objects.get(user=usuario)
            except Avatar.DoesNotExist:
                avatar = Avatar(user=usuario, imagen=informacion["avatar"])
                avatar.save()
            else:
                if informacion["avatar"]:
                    avatar.imagen = informacion["avatar"]
                    avatar.save()

            return render(request, "SupermercadoApp/index.html")

    
    else:
        form = UserEditForm(initial = {"email":usuario.email})
    
    return render(request, "users/profile-edit.html", {"form": form, "user":usuario})

# @login_required
# def agregarAvatar(request):
    form = AvatarFormulario(request.POST, request.FILES)
    print(request.POST, request.FILES)
    
    if request.method == "POST":
        
        if form.is_valid():
            
            informacion = form.cleaned_data
            u = User.objects.get(username = request.user)

            avatar = Avatar(user=u, imagen=informacion["avatar"])
            avatar.save()
            
            return render(request, "SupermercadoApp/index.html")
        
        else:
            form = AvatarFormulario()
        
    return render(request, "SupermercadoApp/agregar-avatar.html", {"form":form})