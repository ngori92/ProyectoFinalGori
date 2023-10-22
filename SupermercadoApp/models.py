from django.db import models
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    domicilio = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='clientes', null=True, blank = True)


    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Domicilio: {self.domicilio}"
            
class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    rut = models.IntegerField()
    categoria_producto = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='proveedores', null=True, blank = True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - RUT: {self.rut} - Categoría: {self.categoria_producto} - Domicilio: {self.domicilio}"

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    tamanio = models.CharField(max_length=20)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', null=True, blank = True)
    
    def __str__(self):
        return f"Nombre: {self.nombre_producto} - Categoría: {self.categoria} - Tamaño: {self.tamanio} - Precio: {self.precio}"
    
class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=30)
    apellido_empleado = models.CharField(max_length=30)
    puesto = models.CharField(max_length=20)
    sueldo = models.IntegerField()
    numero_identidad = models.IntegerField()
    imagen = models.ImageField(upload_to='empleados', null=True, blank = True)
    
    def __str__(self):
        return f"Nombre: {self.nombre_empleado} - Apellido: {self.apellido_empleado} - Puesto: {self.puesto} - Sueldo: {self.sueldo} - CI; {self.numero_identidad}"
