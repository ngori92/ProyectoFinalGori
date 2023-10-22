from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    domicilio = forms.CharField(max_length=40)
    imagen = forms.ImageField(required=False)
    
class ProveedorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    rut = forms.IntegerField()
    categoria_producto = forms.CharField(max_length=20)
    domicilio = forms.CharField(max_length=40)
    imagen = forms.ImageField(required=False)
    
class ProductoFormulario(forms.Form):
    nombre_producto = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=30)
    tamanio = forms.CharField(label="Tamaño", max_length=20)
    precio = forms.IntegerField()
    imagen = forms.ImageField(required=False)

class EmpleadoFormulario(forms.Form):
    nombre_empleado = forms.CharField(max_length=30)
    apellido_empleado = forms.CharField(max_length=30)
    puesto = forms.CharField(max_length=20)
    sueldo = forms.IntegerField()
    numero_identidad = forms.IntegerField()
    imagen = forms.ImageField(required=False)