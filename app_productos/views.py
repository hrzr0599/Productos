from django.shortcuts import render, get_object_or_404, redirect
from .models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm

# Vistas para Proveedor
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/listar_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id_proveedor)
    return render(request, 'proveedores/detalle_proveedor.html', {'proveedor': proveedor})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/formulario_proveedor.html', {'form': form, 'titulo': 'Crear Proveedor'})

def editar_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id_proveedor)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/formulario_proveedor.html', {'form': form, 'titulo': 'Editar Proveedor'})

def borrar_proveedor(request, id_proveedor):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id_proveedor)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('app_productos:listar_proveedores')
    return render(request, 'proveedores/confirmar_borrar.html', {'proveedor': proveedor})

# Vistas para Producto
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

def detalle_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/formulario_producto.html', {'form': form, 'titulo': 'Crear Producto'})

def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/formulario_producto.html', {'form': form, 'titulo': 'Editar Producto'})

def borrar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('app_productos:listar_productos')
    return render(request, 'productos/confirmar_borrar.html', {'producto': producto})