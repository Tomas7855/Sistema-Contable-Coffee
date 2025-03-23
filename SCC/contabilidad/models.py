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
    
    