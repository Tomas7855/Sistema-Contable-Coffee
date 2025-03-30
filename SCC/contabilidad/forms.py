#modificado el 29-03-2025

from django import forms
from .models import MovimientoInventario

class MovimientoInventarioForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        fields = ['producto', 'tipo', 'cantidad', 'motivo']
