from django.db import models

class productos(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    estado = models.CharField(max_length=10, default='Activo')   # ← Agrega esta línea

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productos"