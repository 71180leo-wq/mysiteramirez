# Ubicación exacta: compras/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rutas para listar compras
    path('', views.listasucursal, name='lista_sucursal'),
    path('lista/', views.listasucursal, name='lista_sucursal'),
    
    # Rutas para crear nuevas compras (apuntando al plural)
    path('nueva/', views.nueva_sucursal, name='nueva_sucursal'),
    path('nuevo/', views.nueva_sucursal, name='nuevo_sucursal'),
    
    # Rutas CRUD y baja lógica (apuntando al plural)
    path('editar/<int:id>/', views.editar_sucursal, name='editar_sucursal'),
    path('eliminar/<int:id>/', views.eliminar_sucursal, name='eliminar_sucursal'),
    path('activar/<int:id>/', views.activar_sucursal, name='activar_sucursal'),
]
