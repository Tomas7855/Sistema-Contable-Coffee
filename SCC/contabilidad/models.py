from django.db import models

# Create your models here.

#dudoso el diseño
class CuentaContable(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[
        ('activo', 'Activo'),
        ('pasivo', 'Pasivo'),
        ('patrimonio', 'Patrimonio'),
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    ])
    nivel = models.IntegerField()
    cuenta_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
class AsientoContable(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField()
    
    def __str__(self):
        return f"Asiento {self.id} - {self.fecha}"
    
class DetalleAsiento(models.Model):
    asiento = models.ForeignKey(AsientoContable, on_delete=models.CASCADE, related_name='detalles')
    cuenta = models.ForeignKey(CuentaContable, on_delete=models.CASCADE)
    debe = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    haber = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#Editado el 29-03-2025

from django.core.exceptions import ValidationError


# MODELOS DE INVENTARIO

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.SET_NULL, null=True)
    unidad_medida = models.CharField(max_length=50, default='Unidad')
    stock_actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class MovimientoInventario(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
        ('ajuste', 'Ajuste'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    motivo = models.CharField(max_length=255)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.producto.nombre} ({self.cantidad})"

    def save(self, *args, **kwargs):
        if self.pk is None:  # Solo en creación
            if self.tipo == 'salida' and self.cantidad > self.producto.stock_actual:
                raise ValidationError(f"No hay suficiente stock para realizar la salida. Stock actual: {self.producto.stock_actual}")
            elif self.tipo == 'entrada':
                self.producto.stock_actual += self.cantidad
            elif self.tipo == 'salida':
                self.producto.stock_actual -= self.cantidad
            elif self.tipo == 'ajuste':
                self.producto.stock_actual = self.cantidad
            self.producto.save()

        super().save(*args, **kwargs)

    
    