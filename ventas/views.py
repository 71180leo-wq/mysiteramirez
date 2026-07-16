from django.shortcuts import render, redirect, get_object_or_404
from .models import ventas
from productos.models import productos
from clientes.models import clientes
from django.contrib import messages # Importamos mensajes para avisar si falta algo

# 1. LISTAR VENTAS
def listaventas(request):
    consultaventas = ventas.objects.all().order_by('-id')
    todos_productos = productos.objects.all() 
    todos_clientes = clientes.objects.all()
    
    contexto = {
        'consultaventas': consultaventas,
        'todos_productos': todos_productos,
        'todos_clientes': todos_clientes
    }
    return render(request, 'ventas/lista_ventas.html', contexto)

# 2. CREAR NUEVA VENTA (CORREGIDA)
def nueva_venta(request):
    if request.method == "POST":
        folio = request.POST.get('folio')
        fecha = request.POST.get('fecha')
        subtotal = request.POST.get('subtotal')
        iva = request.POST.get('iva')
        total = request.POST.get('total')
        
        productos_ids = request.POST.getlist('productos')
        clientes_ids = request.POST.getlist('clientes')
        
        # VALIDACIÓN: Evitamos el IntegrityError si el folio u otros campos clave vienen vacíos
        if not folio:
            messages.error(request, "El folio es obligatorio y no puede estar vacío.")
            return redirect('lista_ventas') # O redirige a donde tengas el formulario
            
        # Creamos el registro de manera segura
        nueva = ventas.objects.create(
            folio=folio,
            fecha=fecha if fecha else None, # Si viene vacío, dejamos que guarde el valor por defecto o Null si el modelo lo permite
            subtotal=subtotal if subtotal else 0.0,
            iva=iva if iva else 0.0,
            total=total if total else 0.0
        )
        
        # Guardamos las relaciones ManyToMany
        if productos_ids:
            nueva.productos.set(productos_ids)
        if clientes_ids:
            nueva.clientes.set(clientes_ids)
            
        # La redirección exitosa DEBE estar dentro del bloque POST
        return redirect('lista_ventas')
        
    # Si entran por GET a /pageventas/nuevo/ sin enviar formulario, redirigimos a la lista
    return redirect('lista_ventas')

# 3. EDITAR VENTA (CORREGIDA)
def editar_venta(request, id):
    venta = get_object_or_404(ventas, id=id)
    todos_productos = productos.objects.all()
    todos_clientes = clientes.objects.all()
    
    if request.method == "POST":
        folio = request.POST.get('folio')
        
        if not folio:
            messages.error(request, "El folio es obligatorio para actualizar la venta.")
            return redirect('lista_ventas')
            
        venta.folio = folio
        venta.fecha = request.POST.get('fecha')
        venta.subtotal = request.POST.get('subtotal')
        venta.iva = request.POST.get('iva')
        venta.total = request.POST.get('total')
        venta.save()
        
        productos_ids = request.POST.getlist('productos')
        clientes_ids = request.POST.getlist('clientes')
        venta.productos.set(productos_ids)
        venta.clientes.set(clientes_ids)
        
        return redirect('lista_ventas')
        
    contexto = {
        'venta': venta,
        'todos_productos': todos_productos,
        'todos_clientes': todos_clientes,
    }
    return render(request, 'editar_venta.html', contexto)

# 4. DAR DE BAJA LÓGICA
def eliminar_venta(request, id):
    if request.method == "POST":
        venta = get_object_or_404(ventas, id=id)
        venta.estado = 'Inactivo'
        venta.save()
    return redirect('lista_ventas')

# 5. ACTIVAR VENTA
def activar_venta(request, id):
    if request.method == "POST":
        venta = get_object_or_404(ventas, id=id)
        venta.estado = 'Activo'
        venta.save()
    return redirect('lista_ventas')