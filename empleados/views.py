from django.shortcuts import render, redirect
from .models import empleados


# Create your views here.

def listaempleados(request):
  consultaempledos = empleados.objects.all()
  return render(request, "empleados/empleados.html", {"consultaempledos": consultaempledos})

def creaempleados(request):
  nvoempleados = empleados(
    nombre = request.POST["nombre"],
    apellido =  request.POST["apellido"],
    sexo = request.POST["sexo"],
    tipo = request.POST["tipo"],
    direccion = request.POST["direccion"]
  )

  nvoempleados.save()
  return redirect("/pageempleados/")