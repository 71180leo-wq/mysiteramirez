from django.db import models

# Create your models here.

class productos(models.Model):
    nombre = models.CharField()
    tipo = models.CharField()
    direccion = models.CharField()
    apellido = models.CharField(max_length=100, blank=True, null=True)