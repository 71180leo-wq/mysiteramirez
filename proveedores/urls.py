from django.urls import path
from .views import listaproveedores, creaproveedores

urlpatterns = [ 
path('', listaproveedores),
path('nuevo/',creaproveedores)
]