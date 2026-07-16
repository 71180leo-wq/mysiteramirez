from django.shortcuts import render, redirect, get_object_or_404
from .models import empleados

def listaempleados(request):
    consultaempleados = empleados.objects.all()
    return render(request, "empleados/empleados.html", {"consultaempleados": consultaempleados})

def creaempleados(request):
    if request.method == "POST":
        nvoempleado = empleados(
            nombre = request.POST.get("nombre"),
            apellido = request.POST.get("apellido"),
            sexo = request.POST.get("sexo"),
            tipo = request.POST.get("tipo"),
            direccion = request.POST.get("direccion"),
        )
        nvoempleado.save()
        return redirect('lista_empleados')
    return redirect('lista_empleados')

def editar_empleado(request, pk):
    empleado = get_object_or_404(empleados, pk=pk)
    if request.method == "POST":
        empleado.nombre = request.POST.get("nombre")
        empleado.apellido = request.POST.get("apellido")
        empleado.sexo = request.POST.get("sexo")
        empleado.tipo = request.POST.get("tipo")
        empleado.direccion = request.POST.get("direccion")
        empleado.save()
        return redirect('lista_empleados')
    return render(request, "empleados/editar_empleado.html", {"empleado": empleado})

def eliminar_empleado(request, pk):   # Ahora es "Dar de Baja"
    empleado = get_object_or_404(empleados, pk=pk)
    empleado.estado = 'Inactivo'
    empleado.save()
    return redirect('lista_empleados')