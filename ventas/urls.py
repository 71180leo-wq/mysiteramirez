# Ubicación exacta: ventas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaventas, name='lista_ventas'), 
    path('lista/', views.listaventas, name='lista_venta'), 
    
    # Mapeamos la ruta tanto para 'nueva_venta' como para 'nuevo_venta'
    path('nueva/', views.nueva_venta, name='nueva_venta'),
    path('nuevo/', views.nueva_venta, name='nuevo_venta'), # <-- Esta línea soluciona tu error actual
    
    path('editar/<int:id>/', views.editar_venta, name='editar_venta'),
    path('eliminar/<int:id>/', views.eliminar_venta, name='eliminar_venta'),
    path('activar/<int:id>/', views.activar_venta, name='activar_venta'),
]
