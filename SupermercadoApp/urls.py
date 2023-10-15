from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from SupermercadoApp.views import *
from users.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('about/', about, name="About"),
    path("register", register, name="Register"),
    path("login", login_request, name="Login"),
    path("profile-edit", profileEdit, name="Profile Edit"),
    path("logout", LogoutView.as_view(template_name="SupermercadoApp/logout.html"), name="Logout"),
    
    path('cliente/list', ClienteList.as_view(), name="List"),
    path("cliente/detalle/<int:pk>", ClienteDetalle.as_view(), name="Detail"),
    re_path(r'^nuevo$', ClienteCreacion.as_view(), name="New"),
    path("cliente/editar/<int:pk>", ClienteUpdate.as_view(), name="Edit"),
    path("cliente/eliminar/<int:pk>", ClienteDelete.as_view(), name="Delete"),
    
    path('proveedores/', proveedores, name="Proveedores"),
    path('formulario-proveedores/', formularioProveedores, name="Agregar_proveedor"),
    
    path('productos/', productos, name="Productos"),
    path('formulario-productos/', formularioProductos, name="Agregar_producto"),
    
    path('empleados/', empleados, name="Empleados"),
    path('formulario-empleados/', formularioEmpleados, name="Agregar_empleado"),
]