from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from SupermercadoApp.views import *
from users.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('about/', about, name="About"),
    
    path('cliente/list', ClienteList.as_view(), name="Clientes_List"),
    path("cliente/detalle/<int:pk>", ClienteDetalle.as_view(), name="Cliente_Detail"),
    re_path(r'^cliente_nuevo$', ClienteCreacion.as_view(), name="Cliente_New"),
    path("cliente/editar/<int:pk>", ClienteUpdate.as_view(), name="Cliente_Edit"),
    path("cliente/eliminar/<int:pk>", ClienteDelete.as_view(), name="Cliente_Delete"),
    
    path('proveedor/list', ProveedorList.as_view(), name="Proveedores_List"),
    path("proveedor/detalle/<int:pk>", ProveedorDetalle.as_view(), name="Proveedor_Detail"),
    re_path(r'^proveedor_nuevo$', ProveedorCreacion.as_view(), name="Proveedor_New"),
    path("proveedor/editar/<int:pk>", ProveedorUpdate.as_view(), name="Proveedor_Edit"),
    path("proveedor/eliminar/<int:pk>", ProveedorDelete.as_view(), name="Proveedor_Delete"),
    
    path('producto/list', ProductoList.as_view(), name="Productos_List"),
    path("producto/detalle/<int:pk>", ProductoDetalle.as_view(), name="Producto_Detail"),
    re_path(r'^producto_nuevo$', ProductoCreacion.as_view(), name="Producto_New"),
    path("producto/editar/<int:pk>", ProductoUpdate.as_view(), name="Producto_Edit"),
    path("producto/eliminar/<int:pk>", ProductoDelete.as_view(), name="Producto_Delete"),

    path('empleado/list', EmpleadoList.as_view(), name="Empleados_List"),
    path("empleado/detalle/<int:pk>", EmpleadoDetalle.as_view(), name="Empleado_Detail"),
    re_path(r'^empleado_nuevo$', EmpleadoCreacion.as_view(), name="Empleado_New"),
    path("empleado/editar/<int:pk>", EmpleadoUpdate.as_view(), name="Empleado_Edit"),
    path("empleado/eliminar/<int:pk>", EmpleadoDelete.as_view(), name="Empleado_Delete"),
    
]