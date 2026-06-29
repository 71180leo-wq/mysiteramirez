from django.shortcuts import render, redirect
from .models import usuarios


# Create your views here.

def listausuarios(request):
  consultausuarios = usuarios.objects.all()
  return render(request, "usuarios/usuarios.html", {"consultausuarios": consultausuarios})


def creausuario(request):
  nvousuario = usuarios(
    nombre = request.POST["nombre"],
    apellido = request.POST["apellido"],
    sexo = request.POST["sexo"],
    tipo = request.POST["tipo"],
    direccion = request.POST["direccion"]

  )

  nvousuario.save()
  return redirect("/pageusuarios/")