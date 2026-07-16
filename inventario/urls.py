# Ubicación exacta obligatoria: inventario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rutas para listar inventario
    path('', views.listainventario, name='lista_inventario'),
    path('lista/', views.listainventario, name='lista_inventario'),
    
    # Corregido: Ahora apuntan correctamente a la función de inventario
    path('nueva/', views.nueva_inventario, name='nueva_inventario'),
    path('nuevo/', views.nueva_inventario, name='nuevo_inventario'),
    
    # Rutas CRUD y baja lógica de inventario
    path('editar/<int:id>/', views.editar_inventario, name='editar_inventario'),
    path('eliminar/<int:id>/', views.eliminar_inventario, name='eliminar_inventario'),
    path('activar/<int:id>/', views.activar_inventario, name='activar_inventario'),
]
