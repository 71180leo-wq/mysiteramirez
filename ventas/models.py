
from django.db import models
from productos.models import productos
from clientes.models import clientes

class ventas(models.Model):
    folio = models.CharField(max_length=100)
    fecha = models.DateField(max_length=100)
    subtotal = models.FloatField(max_length=100)
    iva = models.FloatField(max_length=100)
    total = models.FloatField(max_length=100)

    productos = models.ManyToManyField(productos)
    clientes = models.ManyToManyField(clientes)
    

    estado = models.CharField(max_length=20, default='Activo')

    def __str__(self):
        return f"Folio: {self.folio}"
