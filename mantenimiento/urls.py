from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # URLs de vehículos
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('vehiculos/agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculos/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('vehiculos/<int:vehiculo_id>/editar/', views.editar_vehiculo, name='editar_vehiculo'),
    
    # URLs de mantenimientos
    path('mantenimientos/', views.lista_mantenimientos, name='lista_mantenimientos'),
    path('mantenimientos/agregar/', views.agregar_mantenimiento, name='agregar_mantenimiento'),
    path('mantenimientos/agregar/<int:vehiculo_id>/', views.agregar_mantenimiento, name='agregar_mantenimiento_vehiculo'),
    path('mantenimientos/<int:mantenimiento_id>/editar/', views.editar_mantenimiento, name='editar_mantenimiento'),
]