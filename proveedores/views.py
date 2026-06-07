from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def proveedores(request):
  #  return HttpResponse("FORMULARIO DE CIENTES JESUS ")
  return render(request, "proveedores/proveedores.html")


