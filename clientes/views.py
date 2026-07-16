from django.shortcuts import render, redirect, get_object_or_404
from .models import clientes

def listaclientes(request):
    consultaclientes = clientes.objects.all()
    return render(request, "clientes/clientes.html", {"consultaclientes": consultaclientes})

def creaclientes(request):
    if request.method == "POST":
        nvocliente = clientes(
            nombre = request.POST.get("nombre"),
            apellido = request.POST.get("apellido"),
            sexo = request.POST.get("sexo"),
            tipo = request.POST.get("tipo"),
            direccion = request.POST.get("direccion"),
        )
        nvocliente.save()
        return redirect('lista_clientes')
    return redirect('lista_clientes')

def editar_cliente(request, pk):
    cliente = get_object_or_404(clientes, pk=pk)
    if request.method == "POST":
        cliente.nombre = request.POST.get("nombre")
        cliente.apellido = request.POST.get("apellido")
        cliente.sexo = request.POST.get("sexo")
        cliente.tipo = request.POST.get("tipo")
        cliente.direccion = request.POST.get("direccion")
        cliente.save()
        return redirect('lista_clientes')
    return render(request, "clientes/editar_cliente.html", {"cliente": cliente})

def eliminar_cliente(request, pk):   # Ahora es "Dar de Baja"
    cliente = get_object_or_404(clientes, pk=pk)
    cliente.estado = 'Inactivo'
    cliente.save()
    return redirect('lista_clientes')