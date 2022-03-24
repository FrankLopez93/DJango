from django.db import models as mod

# Create your models here.

class Clientes(mod.Model):
    nombre = mod.CharField(max_length = 30)
    direccion = mod.CharField(max_length = 50)
    email = mod.EmailField()
    tfno = mod.CharField(max_length=10)

class Articulos(mod.Model):
    nombre = mod.CharField(max_length = 30)
    seccion = mod.CharField(max_length = 20)
    precio = mod.IntegerField()

class Pedidos(mod.Model):
    numero = mod.IntegerField()
    fecha = mod.DateField()
    entregado = mod.BooleanField()