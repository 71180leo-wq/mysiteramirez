from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaproductos, name='lista_productos'),
    path('nuevo/', views.creaproductos, name='nuevo_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]