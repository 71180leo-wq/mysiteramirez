from django.urls import path
from .views import listausuarios, creausuario

urlpatterns = [ 
path('', listausuarios),
path('nuevo/',creausuario)
]