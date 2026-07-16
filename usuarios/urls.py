from django.urls import path
from . import views

urlpatterns = [
    path('', views.listausuarios, name='lista_usuarios'),
    path('nuevo/', views.creausuario, name='nuevo_usuario'),
    path('editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
]