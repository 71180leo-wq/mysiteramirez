from django.urls import path
from .views import listaempleados, creaempleados

urlpatterns = [ 
path('',listaempleados),
path('nuevo/', creaempleados)
]
