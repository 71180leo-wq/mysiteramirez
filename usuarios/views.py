from django.shortcuts import render, redirect, get_object_or_404
from .models import usuarios

def listausuarios(request):
    consultausuarios = usuarios.objects.all()
    return render(request, "usuarios/usuarios.html", {"consultausuarios": consultausuarios})

def creausuario(request):
    if request.method == "POST":
        nvousuario = usuarios(
            nombre = request.POST.get("nombre"),
            apellido = request.POST.get("apellido"),
            sexo = request.POST.get("sexo"),
            tipo = request.POST.get("tipo"),
            direccion = request.POST.get("direccion"),
        )
        nvousuario.save()
        return redirect('lista_usuarios')
    return redirect('lista_usuarios')

def editar_usuario(request, pk):
    usuario = get_object_or_404(usuarios, pk=pk)
    if request.method == "POST":
        usuario.nombre = request.POST.get("nombre")
        usuario.apellido = request.POST.get("apellido")
        usuario.sexo = request.POST.get("sexo")
        usuario.tipo = request.POST.get("tipo")
        usuario.direccion = request.POST.get("direccion")
        usuario.save()
        return redirect('lista_usuarios')
    return render(request, "usuarios/editar_usuario.html", {"usuario": usuario})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(usuarios, pk=pk)
    usuario.estado = 'Inactivo'
    usuario.save()
    return redirect('lista_usuarios')