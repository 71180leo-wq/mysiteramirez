from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaclientes, name='lista_clientes'),
    path('nuevo/', views.creaclientes, name='nuevo_cliente'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
]