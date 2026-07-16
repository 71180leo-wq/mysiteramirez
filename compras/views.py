from django.shortcuts import render, redirect, get_object_or_404
from productos.models import productos
from proveedores.models import proveedores
from ventas.models import ventas  # Usa el modelo compartido
from django.contrib import messages

# 1. LISTAR COMPRAS
def listacompras(request):
    # Traemos las compras (que están almacenadas en el modelo compartido 'ventas')
    consultacompras = ventas.objects.all().order_by('-id')
    todos_productos = productos.objects.all() 
    todos_proveedores = proveedores.objects.all()
    
    contexto = {
        'consultacompras': consultacompras,     # Sincronizado con el HTML de compras
        'todos_productos': todos_productos,     # Sincronizado con el HTML de compras
        'todos_proveedores': todos_proveedores, # Sincronizado con el HTML de compras
    }
    return render(request, 'compras/lista_compras.html', contexto)


# 2. CREAR NUEVA COMPRA
def nueva_compras(request):
    if request.method == "POST":
        folio = request.POST.get('folio')
        fecha = request.POST.get('fecha')
        subtotal = request.POST.get('subtotal')
        iva = request.POST.get('iva')
        total = request.POST.get('total')
        
        productos_ids = request.POST.getlist('productos')
        proveedores_ids = request.POST.getlist('proveedores')
        
        # Validación básica para no meter folios nulos
        if not folio:
            messages.error(request, "El folio es obligatorio.")
            return redirect('lista_compras')
        
        # Creamos el registro en el modelo ventas usando datos seguros
        nueva = ventas.objects.create(
            folio=folio,
            fecha=fecha if fecha else None,
            subtotal=subtotal if subtotal else 0.0,
            iva=iva if iva else 0.0,
            total=total if total else 0.0,
            estado='Activo'
        )
        
        # Relaciones ManyToMany
        if productos_ids:
            nueva.productos.set(productos_ids)
            
        # Asignamos al campo correspondiente según lo configurado en tu modelo ventas
        if proveedores_ids:
            if hasattr(nueva, 'proveedores'):
                nueva.proveedores.set(proveedores_ids)
            elif hasattr(nueva, 'clientes'):
                nueva.clientes.set(proveedores_ids)
                
        return redirect('lista_compras') # Redirección exitosa en el POST
        
    return redirect('lista_compras') # Redirección si entran por GET


# 3. EDITAR COMPRA
def editar_compras(request, id):
    # Cambié el nombre de la variable local a 'compra' para que machee con tu HTML: {{ compra.folio }}
    compra = get_object_or_404(ventas, id=id) 
    todos_productos = productos.objects.all()
    todos_proveedores = proveedores.objects.all()
    
    if request.method == "POST":
        folio = request.POST.get('folio')
        if not folio:
            messages.error(request, "El folio es obligatorio.")
            return redirect('lista_compras')

        compra.folio = folio
        compra.fecha = request.POST.get('fecha')
        compra.subtotal = request.POST.get('subtotal')
        compra.iva = request.POST.get('iva')
        compra.total = request.POST.get('total')
        compra.save()
        
        productos_ids = request.POST.getlist('productos')
        proveedores_ids = request.POST.getlist('proveedores')
        
        if productos_ids:
            compra.productos.set(productos_ids)
        
        if proveedores_ids:
            if hasattr(compra, 'proveedores'):
                compra.proveedores.set(proveedores_ids)
            elif hasattr(compra, 'clientes'):
                compra.clientes.set(proveedores_ids)
            
        return redirect('lista_compras')
        
    contexto = {
        'compra': compra, # Ahora coincide perfectamente con el HTML de edición
        'todos_productos': todos_productos,
        'todos_proveedores': todos_proveedores,
    }
    return render(request, 'compras/editar_compras.html', contexto)


# 4. DAR DE BAJA LÓGICA
def eliminar_compras(request, id):
    if request.method == "POST":
        compras = get_object_or_404(ventas, id=id)
        compras.estado = 'Inactivo'
        compras.save()
    return redirect('lista_compras')


# 5. ACTIVAR COMPRA
def activar_compras(request, id):
    if request.method == "POST":
        compras = get_object_or_404(ventas, id=id)
        compras.estado = 'Activo'
        compras.save()
    return redirect('lista_compras')