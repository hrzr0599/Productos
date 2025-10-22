from django.urls import path
from . import views

app_name = 'app_productos'

urlpatterns = [
    # Productos
    path('', views.listar_productos, name='listar_productos'),  # Root URL now shows productos
    path('producto/<int:id_producto>/', views.detalle_producto, name='detalle_producto'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/editar/<int:id_producto>/', views.editar_producto, name='editar_producto'),
    path('producto/borrar/<int:id_producto>/', views.borrar_producto, name='borrar_producto'),

    # Proveedores
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedor/<int:id_proveedor>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('proveedor/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedor/editar/<int:id_proveedor>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedor/borrar/<int:id_proveedor>/', views.borrar_proveedor, name='borrar_proveedor'),
]