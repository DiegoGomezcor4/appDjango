from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    codigo = models.CharField(max_length=50,blank=True, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    stock_actual = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedores = models.ManyToManyField(Proveedor, related_name='productos')

    
    def __str__(self):
        return self.nombre

class Compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField(auto_now_add=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'Compra {self.cantidad} de {self.producto.nombre} el {self.fecha}'
    