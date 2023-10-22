from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from SupermercadoApp.forms import *
from SupermercadoApp.models import *
from users.models import *
    
# Create your views here.

def inicio(request):
    return render(request, "SupermercadoApp/index.html")

def about(request):
    return render(request, "SupermercadoApp/about.html")
  
class ClienteList(ListView):
    
    model = Cliente
    template_name = "SupermercadoApp/cliente-list.html"

class ClienteDetalle(LoginRequiredMixin, DetailView):
    
    model = Cliente
    template_name = "SupermercadoApp/cliente-detalle.html"
    
class ClienteCreacion(LoginRequiredMixin, CreateView):
    
    model = Cliente
    template_name = "SupermercadoApp/cliente-form.html"
    success_url = reverse_lazy("Clientes_List")
    fields = ["nombre", "apellido", "edad", "domicilio", "imagen"]
    
class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = "SupermercadoApp/cliente-form.html"
    success_url = reverse_lazy("Clientes_List")
    fields = ["nombre", "apellido", "edad", "domicilio", "imagen"]

class ClienteDelete(LoginRequiredMixin, DeleteView):
    
    model = Cliente
    template_name = "SupermercadoApp/cliente-confirm-delete.html"
    success_url = reverse_lazy("Clientes_List")
    
class ProveedorList(ListView):
    model = Proveedor
    template_name = "SupermercadoApp/proveedor-list.html"
    
class ProveedorDetalle(LoginRequiredMixin, DetailView):
    
    model = Proveedor
    template_name = "SupermercadoApp/proveedor-detalle.html"
    
class ProveedorCreacion(LoginRequiredMixin, CreateView):
    
    model = Proveedor
    template_name = "SupermercadoApp/proveedor-form.html"
    success_url = reverse_lazy("Proveedores_List")
    fields = ["nombre", "rut", "categoria_producto", "domicilio", "imagen"]
    
class ProveedorUpdate(LoginRequiredMixin, UpdateView):
    model = Proveedor
    template_name = "SupermercadoApp/proveedor-form.html"
    success_url = reverse_lazy("Proveedores_List")
    fields = ["nombre", "rut", "categoria_producto", "domicilio", "imagen"]

class ProveedorDelete(LoginRequiredMixin, DeleteView):
    
    model = Proveedor
    template_name = "SupermercadoApp/proveedor-confirm-delete.html"
    success_url = reverse_lazy("Proveedores_List")
    
class ProductoList(ListView):
    model = Producto
    template_name = "SupermercadoApp/producto-list.html"
    
class ProductoDetalle(LoginRequiredMixin, DetailView):
    
    model = Producto
    template_name = "SupermercadoApp/producto-detalle.html"
    
class ProductoCreacion(LoginRequiredMixin, CreateView):
    
    model = Producto
    template_name = "SupermercadoApp/producto-form.html"
    success_url = reverse_lazy("Productos_List")
    fields = ["nombre_producto", "categoria", "tamanio", "precio", "imagen"]
    
class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "SupermercadoApp/producto-form.html"
    success_url = reverse_lazy("Productos_List")
    fields = ["nombre_producto", "categoria", "tamanio", "precio", "imagen"]

class ProductoDelete(LoginRequiredMixin, DeleteView):
    
    model = Producto
    template_name = "SupermercadoApp/producto-confirm-delete.html"
    success_url = reverse_lazy("Productos_List")
    
class EmpleadoList(ListView):
    model = Empleado
    template_name = "SupermercadoApp/empleado-list.html"
    
class EmpleadoDetalle(LoginRequiredMixin, DetailView):
    
    model = Empleado
    template_name = "SupermercadoApp/empleado-detalle.html"
    
class EmpleadoCreacion(LoginRequiredMixin, CreateView):
    
    model = Empleado
    template_name = "SupermercadoApp/empleado-form.html"
    success_url = reverse_lazy("Empleados_List")
    fields = ["nombre_empleado", "apellido_empleado", "puesto", "sueldo", "numero_identidad", "imagen"]
    
class EmpleadoUpdate(LoginRequiredMixin, UpdateView):
    model = Empleado
    template_name = "SupermercadoApp/empleado-form.html"
    success_url = reverse_lazy("Empleados_List")
    fields = ["nombre_empleado", "apellido_empleado", "puesto", "sueldo", "numero_identidad"]

class EmpleadoDelete(LoginRequiredMixin, DeleteView):
    
    model = Empleado
    template_name = "SupermercadoApp/empleado-confirm-delete.html"
    success_url = reverse_lazy("Empleados_List")
