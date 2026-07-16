from django.shortcuts import render, redirect, get_object_or_404
from .models import proveedores

def listaproveedores(request):
    consultaproveedores = proveedores.objects.all()
    return render(request, "proveedores/proveedores.html", {"consultaproveedores": consultaproveedores})

def creaproveedores(request):
    if request.method == "POST":
        nvoproveedor = proveedores(
            nombre = request.POST.get("nombre"),
            apellido = request.POST.get("apellido"),
            sexo = request.POST.get("sexo"),
            tipo = request.POST.get("tipo"),
            direccion = request.POST.get("direccion"),
        )
        nvoproveedor.save()
        return redirect('lista_proveedores')
    return redirect('lista_proveedores')

def editar_proveedor(request, pk):
    proveedor = get_object_or_404(proveedores, pk=pk)
    if request.method == "POST":
        proveedor.nombre = request.POST.get("nombre")
        proveedor.apellido = request.POST.get("apellido")
        proveedor.sexo = request.POST.get("sexo")
        proveedor.tipo = request.POST.get("tipo")
        proveedor.direccion = request.POST.get("direccion")
        proveedor.save()
        return redirect('lista_proveedores')
    return render(request, "proveedores/editar_proveedor.html", {"proveedor": proveedor})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(proveedores, pk=pk)
    proveedor.estado = 'Inactivo'
    proveedor.save()
    return redirect('lista_proveedores')