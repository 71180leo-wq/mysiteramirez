# Ubicación exacta obligatoria: inventario/views.py
from django.shortcuts import render, redirect, get_object_or_404
from productos.models import productos
from proveedores.models import proveedores
from ventas.models import ventas  # Usa el modelo de base de datos compartido

# 1. LISTAR INVENTARIO
def listainventario(request):
    consultaventas = ventas.objects.all().order_by('-id')
    todos_productos = productos.objects.all() 
    todos_proveedores = proveedores.objects.all()
    todos_ventas = ventas.objects.all()
    
    contexto = {
        'consultaventas': consultaventas,
        'todos_productos': todos_productos,
        'todos_clientes': todos_proveedores,
        'todos_ventas': todos_ventas,
    }
    # Corregido: Busca el archivo en la carpeta de inventario
    return render(request, 'inventario/lista_inventario.html', contexto)

# 2. CREAR NUEVO REGISTRO EN INVENTARIO
def nueva_inventario(request):
    if request.method == "POST":
        folio = request.POST.get('folio')
        fecha = request.POST.get('fecha')
        subtotal = request.POST.get('subtotal')
        iva = request.POST.get('iva')
        total = request.POST.get('total')
        
        productos_ids = request.POST.getlist('productos')
        proveedores_ids = request.POST.getlist('proveedores')
        
        nueva = ventas.objects.create(
            folio=folio,
            fecha=fecha,
            subtotal=subtotal,
            iva=iva,
            total=total
        )
        
        nueva.productos.set(productos_ids)
        
        if hasattr(nueva, 'proveedores'):
            nueva.proveedores.set(proveedores_ids)
        elif hasattr(nueva, 'clientes'):
            nueva.clientes.set(proveedores_ids)
        
    return redirect('lista_inventario')

# 3. EDITAR INVENTARIO
def editar_inventario(request, id):
    inventario_item = get_object_or_404(ventas, id=id)
    todos_productos = productos.objects.all()
    todos_proveedor = proveedores.objects.all()
    
    if request.method == "POST":
        inventario_item.folio = request.POST.get('folio')
        inventario_item.fecha = request.POST.get('fecha')
        inventario_item.subtotal = request.POST.get('subtotal')
        inventario_item.iva = request.POST.get('iva')
        inventario_item.total = request.POST.get('total')
        inventario_item.save()
        
        productos_ids = request.POST.getlist('productos')
        proveedores_ids = request.POST.getlist('proveedores')
        inventario_item.productos.set(productos_ids)
        
        if hasattr(inventario_item, 'proveedores'):
            inventario_item.proveedores.set(proveedores_ids)
        elif hasattr(inventario_item, 'clientes'):
            inventario_item.clientes.set(proveedores_ids)
            
        return redirect('lista_inventario')
        
    contexto = {
        'compras': inventario_item,  # Mantenemos 'compras' por si tu HTML de edición hereda esa variable
        'todos_productos': todos_productos,
        'todos_proveedor': todos_proveedor,
    }
    return render(request, 'inventario/editar_compras.html', contexto)

# 4. DAR DE BAJA LÓGICA EN INVENTARIO
def eliminar_inventario(request, id):
    if request.method == "POST":
        inventario_item = get_object_or_404(ventas, id=id)
        inventario_item.estado = 'Inactivo'
        inventario_item.save()
    return redirect('lista_inventario')

# 5. ACTIVAR REGISTRO EN INVENTARIO
def activar_inventario(request, id):
    if request.method == "POST":
        inventario_item = get_object_or_404(ventas, id=id)
        inventario_item.estado = 'Activo'
        inventario_item.save()
    return redirect('lista_inventario')
