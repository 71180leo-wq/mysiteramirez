from django.shortcuts import render, redirect
from .models import clientes

# Create your views here.

def listaclientes(request):
  #  return HttpResponse("FORMULARIO DE CIENTES JESUS ")
  return render(request, "clientes/clientes.html")

def creaclientes(request):
  nvocliente = clientes(
    nombre = request.POST["nombres"],
    apellido =  request.POST["apellido"],
    sexo = request.POST["sexo"],
    tipo = request.POST["tipo"],
    direccion = request.POST["direccion"]
  )

  nvocliente.save()
  return redirect("/pageclientes/")


