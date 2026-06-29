from django.urls import path
from .views import listaproductos, creaproductos

urlpatterns = [ 
path('', listaproductos),
path('nuevo/', creaproductos)
]