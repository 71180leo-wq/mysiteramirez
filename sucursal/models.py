from django.db import models
from empleados.models import empleados 
from django.utils import timezone 

class sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=100, default='General')
    estado = models.CharField(max_length=20, default='Activo')
    
    
    fecha_creacion = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.nombre