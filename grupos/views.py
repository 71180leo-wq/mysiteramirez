# Ubicación exacta: grupos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Grupos

# 1. LISTAR GRUPOS
def listagrupos(request):
    consultagrupos = Grupos.objects.all().order_by('-id')
    # Corregido: Cambiado "grupos.html" por "lista_grupos.html" para que coincida con tu VS Code
    return render(request, "grupos/lista_grupos.html", {"consultagrupos": consultagrupos})

# 2. CREAR NUEVO GRUPO
def creagrupos(request):
    if request.method == "POST":
        nvogrupo = Grupos(
            nombre = request.POST.get("nombre"),
            apellido = request.POST.get("apellido"),
            sexo = request.POST.get("sexo"),
            tipo = request.POST.get("tipo"),
            direccion = request.POST.get("direccion"),
            estado = 'Activo' # Se asigna por defecto al crear
        )
        nvogrupo.save()
    return redirect("lista_grupos")

# 3. DAR DE BAJA LÓGICA (Nuevo para Grupos)
def eliminar_grupos(request, id):
    if request.method == "POST":
        grupo = get_object_or_404(Grupos, id=id)
        grupo.estado = 'Inactivo'
        grupo.save()
    return redirect("lista_grupos")

# 4. ACTIVAR GRUPO (Nuevo para Grupos)
def activar_grupos(request, id):
    if request.method == "POST":
        grupo = get_object_or_404(Grupos, id=id)
        grupo.estado = 'Activo'
        grupo.save()
    return redirect("lista_grupos")
