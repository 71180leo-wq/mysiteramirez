from django.shortcuts import render, redirect
from .models import productos


# Create your views here.

def listaproductos(request):
  consultaproductos = productos.objects.all()
  return render(request, "productos/productos.html",{"consultaproductos": consultaproductos})

def creaproductos(request):
  nvoproducto = productos (
    nombre = request.POST["npmbre"],
    tipo = request.POST["tipo"],
    direccion = request.POST["direccion"]
  )
  nvoproducto.save()
  return redirect("/pageproductos/")

