from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaempleados, name='lista_empleados'),
    path('nuevo/', views.creaempleados, name='nuevo_empleado'),
    path('editar/<int:pk>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar/<int:pk>/', views.eliminar_empleado, name='eliminar_empleado'),
]