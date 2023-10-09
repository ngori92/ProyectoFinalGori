from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    domicilio = models.CharField(max_length=40)
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    rut = models.IntegerField()
    categoria_producto = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=40)
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    tamanio = models.CharField(max_length=20)
    precio = models.IntegerField()

class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=30)
    apellido_empleado = models.CharField(max_length=30)
    puesto = models.CharField(max_length=20)
    sueldo = models.IntegerField()
    numero_identidad = models.IntegerField()