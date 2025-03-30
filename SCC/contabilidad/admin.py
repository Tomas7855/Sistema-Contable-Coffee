from django.contrib import admin
from .models import CuentaContable, AsientoContable, DetalleAsiento

admin.site.register(CuentaContable)
admin.site.register(AsientoContable)
admin.site.register(DetalleAsiento)

#Editado el 29-03-2025
from .models import CategoriaProducto, Producto, MovimientoInventario

admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(MovimientoInventario)
