from django import forms
from .models import Vehiculo, Mantenimiento

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['placa', 'marca', 'modelo', 'año', 'kilometraje']
        widgets = {
            'placa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: ABC123'
            }),
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Toyota'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Corolla'
            }),
            'año': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1990',
                'max': '2030'
            }),
            'kilometraje': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'Kilometraje actual'
            })
        }
        labels = {
            'placa': 'Placa del vehículo',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'año': 'Año',
            'kilometraje': 'Kilometraje actual'
        }

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['vehiculo', 'tipo', 'descripcion', 'fecha', 'kilometraje_actual', 'costo', 'taller', 'completado']
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe el mantenimiento realizado...'
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'kilometraje_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'costo': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.01'
            }),
            'taller': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del taller'
            }),
            'completado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'vehiculo': 'Vehículo',
            'tipo': 'Tipo de mantenimiento',
            'descripcion': 'Descripción del trabajo',
            'fecha': 'Fecha del mantenimiento',
            'kilometraje_actual': 'Kilometraje al momento del mantenimiento',
            'costo': 'Costo del mantenimiento',
            'taller': 'Nombre del taller donde se realizará',
            'completado': 'Mantenimiento completado'
        }