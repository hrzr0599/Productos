from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, help_text="Nombre del proveedor")
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

class Producto(models.Model):
    CATEGORIAS = [
        ('ELECTRONICA', 'Electrónica'),
        ('ROPA', 'Ropa'),
        ('ALACENA', 'Alacena'),
        ('REFRIGERADOS', 'Refrigerados'),
        ('HIGIENE, SALUD, Y BELLEZA', 'Higiene, salud, y belleza'),
        ('HOGAR', 'Hogar'),
        ('DEPORTES', 'Deportes'),
        ('OTROS', 'Otros'),
    ]
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, help_text="Nombre del producto")
    categoria = models.CharField(max_length=100, choices=CATEGORIAS, default='OTROS')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    imagen_url = models.URLField(verbose_name="URL de la imagen", blank=True, null=True, help_text="Enlace a la imagen del producto")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"