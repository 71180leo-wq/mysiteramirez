from django.db import models

class usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    estado = models.CharField(max_length=10, default='Activo')   # ← Agrega esta línea

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Usuarios"