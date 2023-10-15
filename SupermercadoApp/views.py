from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from SupermercadoApp.forms import *
from SupermercadoApp.models import *
    
# Create your views here.
@login_required
def inicio(request):
    
    return render(request, "SupermercadoApp/index.html")

def about(request):
    return render(request, "SupermercadoApp/about.html")

# def login_request(request):
    
#     if request.method == "POST":
#         form = AuthenticationForm(request, data = request.POST)
        
#         if form.is_valid():
#             usuario = form.cleaned_data.get("username")
#             contra = form.cleaned_data.get("password")
            
#             user = authenticate(username = usuario, password = contra)
            
#             if user is not None:
#                 login(request, user)
                
#                 return render(request, "SupermercadoApp/index.html", {"mensaje":f"Bienvenido {usuario}!"})
#             else:
                
#                 return render(request, "SupermercadoApp/index.html", {"mensaje":"Error, datos incorrectos."})
            
#         else:
            
#             return render(request, "SupermercadoApp/index.html", {"mensaje": "Error en el formulario."})

#     form = AuthenticationForm()
    
#     return render(request, "SupermercadoApp/login.html", {"form": form})

# def register(request):
    
#     if request.method == "POST":
        
#         form = UserRegisterForm(request.POST)
        
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             form.save()
#             return render(request, "SupermercadoApp/index.html", {"mensaje":f"Usuario '{username}' creado con éxito."})
        
#     else:
#         form = UserRegisterForm()
        
#     return render(request, "SupermercadoApp/register.html", {"form":form})

# def profileEdit(request):
    
    user = request.user
    
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            
            informacion = form.cleaned_data
            
            user.email = informacion["email"]
            user.password1 = informacion["password1"]
            user.password2 = informacion["password1"]
            user.save()
            
            return render(request, "SupermercadoApp/index.html")
    
    else:
        form = UserEditForm(initial = {"email":user.email})
    
    return render(request, "SupermercadoApp/profile-edit.html", {"form": form, "user":user})
            
     
def proveedores(request):
    return render(request, "SupermercadoApp/proveedores.html")

def formularioProveedores(request):
    
    if request.method == "POST":
        
        formularioProveedor = ProveedorFormulario(request.POST)
        
        if formularioProveedor.is_valid():
            
            informacion = formularioProveedor.cleaned_data
            proveedor = Proveedor(nombre = informacion["nombre"], rut = informacion["rut"], categoria_producto = informacion["categoria_producto"], domicilio = informacion["domicilio"])
            proveedor.save()
            return render(request, "SupermercadoApp/index.html")
        
    else: 
        formularioProveedor = ProveedorFormulario()
        
    return render(request, "SupermercadoApp/formulario-proveedores.html", {"formularioProveedor": formularioProveedor})

def productos(request):
    return render(request, "SupermercadoApp/productos.html")

def formularioProductos(request):
    
    if request.method == "POST":
        
        formularioProducto = ProductoFormulario(request.POST)
        
        if formularioProducto.is_valid():
            
            informacion = formularioProducto.cleaned_data
            producto = Producto(nombre_producto = informacion["nombre_producto"], categoria_producto = informacion["categoria_producto"], tamanio = informacion["tamanio"], precio = informacion["precio"])
            producto.save()
            return render(request, "SupermercadoApp/index.html")
        
    else: 
        formularioProducto = ProductoFormulario()
        
    return render(request, "SupermercadoApp/formulario-productos.html", {"formularioProducto": formularioProducto})
    
def empleados(request):
    return render(request, "SupermercadoApp/empleados.html")

def formularioEmpleados(request):
    
    if request.method == "POST":
        
        formularioEmpleado = EmpleadoFormulario(request.POST)
        
        if formularioEmpleado.is_valid():
            
            informacion = formularioEmpleado.cleaned_data
            empleado = Empleado(nombre_empleado = informacion["nombre_empleado"], apellido_empleado = informacion["apellido_empleado"], puesto = informacion["puesto"], salario = informacion["salario"], numero_identidad = informacion["numero_identidad"])
            empleado.save()
            return render(request, "SupermercadoApp/index.html")
        
    else: 
        formularioEmpleado = EmpleadoFormulario()
        
    return render(request, "SupermercadoApp/formulario-empleados.html", {"formularioEmpleado": formularioEmpleado})

class ClienteList(ListView):
    
    model = Cliente
    template_name = "SupermercadoApp/cliente-list.html"

class ClienteDetalle(DetailView):
    
    model = Cliente
    template_name = "SupermercadoApp/cliente-detalle.html"
    
class ClienteCreacion(CreateView):
    
    model = Cliente
    template_name = "SupermercadoApp/cliente-form.html"
    success_url = reverse_lazy("List")
    fields = ["nombre", "apellido", "edad", "domicilio"]
    
class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = "SupermercadoApp/cliente-form.html"
    success_url = reverse_lazy("List")
    fields = ["nombre", "apellido", "edad", "domicilio"]

class ClienteDelete(DeleteView):
    
    model = Cliente
    template_name = "SupermercadoApp/cliente-confirm-delete.html"
    success_url = reverse_lazy("List")