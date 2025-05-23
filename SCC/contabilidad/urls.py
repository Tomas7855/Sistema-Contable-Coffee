from django.urls import path
from . import views

urlpatterns = [
    path('movimiento/', views.registrar_movimiento, name='registrar_movimiento'),
    path('reporte/', views.reporte_inventario, name='reporte_inventario'),
    path('historial/<int:producto_id>/', views.historial_producto, name='historial_producto'),
]
