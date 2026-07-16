from django.shortcuts import render, redirect, get_object_or_404
from .models import productos

def listaproductos(request):
    consultaproductos = productos.objects.all()
    return render(request, "productos/productos.html", {"consultaproductos": consultaproductos})

def creaproductos(request):
    if request.method == "POST":
        nvoproducto = productos(
            nombre = request.POST.get("nombre"),
            tipo = request.POST.get("tipo"),
            direccion = request.POST.get("direccion"),
        )
        nvoproducto.save()
        return redirect('lista_productos')
    return redirect('lista_productos')

def editar_producto(request, pk):
    producto = get_object_or_404(productos, pk=pk)
    if request.method == "POST":
        producto.nombre = request.POST.get("nombre")
        producto.tipo = request.POST.get("tipo")
        producto.direccion = request.POST.get("direccion")
        producto.save()
        return redirect('lista_productos')
    return render(request, "productos/editar_producto.html", {"producto": producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(productos, pk=pk)
    producto.estado = 'Inactivo'
    producto.save()
    return redirect('lista_productos')