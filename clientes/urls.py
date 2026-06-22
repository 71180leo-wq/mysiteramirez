from django.urls import path
from .views import listaclientes, creaclientes 

urlpatterns = [ 
  path('', listaclientes),
  path('nuevo/', creaclientes)
]