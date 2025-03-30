from django.shortcuts import render

# creado el 29-03-2025

from django.shortcuts import render, redirect
from .forms import MovimientoInventarioForm
from django.contrib import messages

def registrar_movimiento(request):
    if request.method == 'POST':
        form = MovimientoInventarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Movimiento registrado exitosamente.')
                return redirect('registrar_movimiento')
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = MovimientoInventarioForm()
    
    return render(request, 'contabilidad/registrar_movimiento.html', {'form': form})


# Vista reporte de Inventario Editado el 29-03-2025
from django.db.models import Sum
from .models import Producto, MovimientoInventario
from django.utils import timezone
from datetime import datetime

def reporte_inventario(request):
    productos = Producto.objects.all()
    movimientos = MovimientoInventario.objects.all()

    tipo = request.GET.get('tipo')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if tipo:
        movimientos = movimientos.filter(tipo=tipo)
    if fecha_inicio:
        movimientos = movimientos.filter(fecha__gte=fecha_inicio)
    if fecha_fin:
        movimientos = movimientos.filter(fecha__lte=fecha_fin)

    # Datos para el gráfico
    resumen = movimientos.values('tipo').annotate(total=Sum('cantidad'))

    tipos = ['entrada', 'salida', 'ajuste']
    datos_grafico = {tipo: 0 for tipo in tipos}
    for r in resumen:
        datos_grafico[r['tipo']] = float(r['total'])

    context = {
        'productos': productos,
        'movimientos': movimientos,
        'datos_grafico': datos_grafico,
        'filtros': {
            'tipo': tipo,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
        }
    }
    return render(request, 'contabilidad/reporte_inventario.html', context)


#Historial de Movimientos
from django.shortcuts import get_object_or_404
from .models import Producto, MovimientoInventario

def historial_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    movimientos = MovimientoInventario.objects.filter(producto=producto).order_by('-fecha')

    return render(request, 'contabilidad/historial_producto.html', {
        'producto': producto,
        'movimientos': movimientos
    })

