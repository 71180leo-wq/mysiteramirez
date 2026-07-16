from django.shortcuts import render, redirect, get_object_or_404
from empleados.models import empleados
from sucursal.models import sucursal

# 1. LISTAR SUCURSALES
def listasucursal(request):
    consultasucursal = sucursal.objects.all().order_by('-id')
    todos_empleados = empleados.objects.all() 
  
    contexto = {
        'consultasucursal': consultasucursal,
        'todos_empleados': todos_empleados,
    }
    return render(request, 'sucursal/lista_sucursal.html', contexto)

# 2. CREAR NUEVA SUCURSAL (Corregido de forma segura y directa)
def nueva_sucursal(request):
    if request.method == "POST":
        nueva = sucursal()
        
        # Asignación directa por el nombre del atributo en el Modelo
        nueva.nombre = request.POST.get('nombre')
        nueva.direccion = request.POST.get('direccion')
        nueva.telefono = request.POST.get('telefono')
        
        # Obtenemos la ciudad. Si viene vacía del formulario, le ponemos "General" por defecto
        ciudad_input = request.POST.get('ciudad')
        nueva.ciudad = ciudad_input if ciudad_input else "General"
        
        nueva.estado = 'Activo'
        nueva.save() # Ahora guardará perfectamente en PostgreSQL sin errores de Null
        
    return redirect('lista_sucursal')

# 3. EDITAR SUCURSAL (Corregido de forma segura y directa)
def editar_sucursal(request, id):
    instancia_sucursal = get_object_or_404(sucursal, id=id)
    
    if request.method == "POST":
        # Asignación directa por el nombre del atributo al editar
        instancia_sucursal.nombre = request.POST.get('nombre')
        instancia_sucursal.direccion = request.POST.get('direccion')
        instancia_sucursal.telefono = request.POST.get('telefono')
        
        ciudad_input = request.POST.get('ciudad')
        instancia_sucursal.ciudad = ciudad_input if ciudad_input else "General"
            
        instancia_sucursal.save()
        return redirect('lista_sucursal')
        
    contexto = {
        'sucursal': instancia_sucursal,
    }
    return render(request, 'sucursal/editar_sucursal.html', contexto)

# 4. DAR DE BAJA LÓGICA
def eliminar_sucursal(request, id):
    if request.method == "POST":
        instancia_sucursal = get_object_or_404(sucursal, id=id)
        instancia_sucursal.estado = 'Inactivo'
        instancia_sucursal.save()
    return redirect('lista_sucursal')

# 5. ACTIVAR SUCURSAL
def activar_sucursal(request, id):
    if request.method == "POST":
        instancia_sucursal = get_object_or_404(sucursal, id=id)
        instancia_sucursal.estado = 'Activo'
        instancia_sucursal.save()
    return redirect('lista_sucursal')