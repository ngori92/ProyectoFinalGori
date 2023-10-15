from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    domicilio = forms.CharField(max_length=40)
    
class ProveedorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    rut = forms.IntegerField()
    categoria_producto = forms.CharField(max_length=20)
    domicilio = forms.CharField(max_length=40)
    
class ProductoFormulario(forms.Form):
    nombre_producto = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=30)
    tamanio = forms.CharField(max_length=20)
    precio = forms.IntegerField()

class EmpleadoFormulario(forms.Form):
    nombre_empleado = forms.CharField(max_length=30)
    apellido_empleado = forms.CharField(max_length=30)
    puesto = forms.CharField(max_length=20)
    sueldo = forms.IntegerField()
    numero_identidad = forms.IntegerField()