from django.db import models

# Create your models here.

class productos(models.Model):
    nombre = models.CharField()
    apellido =  models.CharField()
    sexo = models.CharField()
    tipo = models.CharField()
    direccion = models.CharField()
