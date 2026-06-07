from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def productos(request):
  #  return HttpResponse("FORMULARIO DE CIENTES JESUS ")
  return render(request, "productos/productos.html")
