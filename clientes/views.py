from django.shortcuts import render
from django.http import HttpResponse
from .models import clientes

# Create your views here.

def listaclientes(request):
  #  return HttpResponse("FORMULARIO DE CIENTES JESUS ")
  return render(request, "clientes/clientes.html")

