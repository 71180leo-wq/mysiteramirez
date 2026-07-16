from django.db import models

# Create your models here.

class usuarios(models.Model):
    nombre = models.CharField()
    apellido =  models.CharField()
    sexo = models.CharField()
    tipo = models.CharField()
    direccion = models.CharField()

class grupos(models.Model):
    nombre = models.CharField()
    apellido =  models.CharField()
    sexo = models.CharField()
    tipo = models.CharField()
    direccion = models.CharField()
    usuarios = models.ForeignKey(usuarios, on_delete= models.CASCADE, related_name="grupos")
