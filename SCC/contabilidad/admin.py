from django.contrib import admin
from .models import CuentaContable, AsientoContable, DetalleAsiento

admin.site.register(CuentaContable)
admin.site.register(AsientoContable)
admin.site.register(DetalleAsiento)
