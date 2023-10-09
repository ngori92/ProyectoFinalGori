from django.urls import path
from SupermercadoApp.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('about/', about, name="About"),
    path('clientes/', clientes, name="Clientes"),
    path('proveedores/', proveedores, name="Proveedores"),
    path('productos/', productos, name="Productos"),
    path('empleados/', empleados, name="Empleados"),
]
