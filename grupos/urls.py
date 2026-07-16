# Ubicación exacta: grupos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rutas para listar que solucionan tu NoReverseMatch
    path('', views.listagrupos, name='lista_grupos'),
    path('lista/', views.listagrupos, name='lista_grupo'),
    
    # Ruta para crear
    path('crear/', views.creagrupos, name='nuevo_grupo'),
    path('nuevo/', views.creagrupos, name='nuevo_grupo'),
    
    # Rutas para dar de baja lógica y activar de nuevo
    path('eliminar/<int:id>/', views.eliminar_grupos, name='eliminar_grupo'),
    path('activar/<int:id>/', views.activar_grupos, name='activar_grupo'),
]
