from django.shortcuts import render, redirect
from .models import clientes

# Create your views here.

def listaclientes(request):
  consultaclientes = clientes.objects.all()
  return render(request, "clientes/clientes.html", {"consultaclientes": consultaclientes})

def creaclientes(request):
  nvocliente = clientes(
    nombre = request.POST["nombre"],
    apellido =  request.POST["apellido"],
    sexo = request.POST["sexo"],
    tipo = request.POST["tipo"],
    direccion = request.POST["direccion"]
  )

  nvocliente.save()
  return redirect("/pageclientes/")


