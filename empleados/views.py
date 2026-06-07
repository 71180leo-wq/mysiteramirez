from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def empleados(request):
  #  return HttpResponse("FORMULARIO DE CIENTES JESUS ")
  return render(request, "empleados/empleados.html")