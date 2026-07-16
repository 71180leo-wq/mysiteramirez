# Ubicación exacta: compras/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rutas para listar compras
    path('', views.listacompras, name='lista_compras'),
    path('lista/', views.listacompras, name='lista_compra'),
    
    # Rutas para crear nuevas compras (apuntando al plural)
    path('nueva/', views.nueva_compras, name='nueva_compra'),
    path('nuevo/', views.nueva_compras, name='nuevo_compra'),
    
    # Rutas CRUD y baja lógica (apuntando al plural)
    path('editar/<int:id>/', views.editar_compras, name='editar_compra'),
    path('eliminar/<int:id>/', views.eliminar_compras, name='eliminar_compra'),
    path('activar/<int:id>/', views.activar_compras, name='activar_compra'),
]
