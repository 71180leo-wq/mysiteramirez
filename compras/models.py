# Ubicación: compras/models.py
from django.db import models
from productos.models import productos
from proveedores.models import proveedores

class compras(models.Model):
    # ... tus otros campos (folio, fecha, subtotal, iva, total) ...
    folio = models.CharField(max_length=100)
    fecha = models.DateField(max_length=100)
    subtotal = models.FloatField(max_length=100)
    iva = models.FloatField(max_length=100)
    total = models.FloatField(max_length=100)
    estado = models.CharField(max_length=20, default='Activo')

    
    productos = models.ManyToManyField(
        productos, 
        related_name='compras_productos_rel',
        db_table='tbl_compras_productos'  
    )
    proveedores = models.ManyToManyField(
        proveedores, 
        related_name='compras_proveedores_rel',
        db_table='tbl_compras_proveedores' 
    )
