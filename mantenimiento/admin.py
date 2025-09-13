from django.contrib import admin
from .models import Vehiculo, Mantenimiento

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['placa', 'marca', 'modelo', 'año', 'kilometraje']
    search_fields = ['placa', 'marca', 'modelo']
    list_filter = ['marca', 'año']

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ['vehiculo', 'tipo', 'fecha', 'costo', 'completado']
    list_filter = ['tipo', 'completado', 'fecha']
    search_fields = ['vehiculo__placa', 'descripcion']
    date_hierarchy = 'fecha'