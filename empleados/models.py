from django.db import models

# Create your models here.

class empleados(models.Model):
    nombre = models.CharField()
    apellido =  models.CharField()
    sexo = models.CharField()
    tipo = models.CharField()
    direccion = models.CharField()

class nomina(models.Model):
    nombre = models.CharField()
    apellido =  models.CharField()
    sexo = models.CharField()
    tipo = models.CharField()
    direccion = models.CharField()
    empleados = models.ForeignKey(empleados, on_delete=models.CASCADE, related_name="nominas")

