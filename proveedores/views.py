from django.shortcuts import render, redirect
from .models import proveedores


# Create your views here.

def listaproveedores(request):
  consultaproveedores = proveedores.objects.all()
  return render(request, "proveedores/proveedores.html", {"consultaproveedores": consultaproveedores})

def creaproveedores(request):
  nvoproveedor = proveedores(
    nombre = request.POST["nombre"],
    apellido = request.POST["apellido"],
    sexo = request.POST["sexo"],
    tipo = request.POST["tipo"],
    direccion = request.POST["direccion"]

  )

  nvoproveedor.save()
  return redirect("/pageproveedores/")
