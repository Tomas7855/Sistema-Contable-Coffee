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
from .models import Producto

def reporte_inventario(request):
    productos = Producto.objects.all()
    return render(request, 'contabilidad/reporte_inventario.html', {'productos': productos})

