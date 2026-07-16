from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaproveedores, name='lista_proveedores'),
    path('nuevo/', views.creaproveedores, name='nuevo_proveedor'),
    path('editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
]