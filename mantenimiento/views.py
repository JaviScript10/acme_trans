from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Vehiculo, Mantenimiento
from .forms import VehiculoForm, MantenimientoForm
from django.db.models import Q

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('placa')
    return render(request, 'mantenimiento/lista_vehiculos.html', {
        'vehiculos': vehiculos
    })

def detalle_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    mantenimientos = Mantenimiento.objects.filter(vehiculo=vehiculo).order_by('-fecha')
    
    # Calcular costo total
    costo_total = sum(m.costo for m in mantenimientos)
    
    return render(request, 'mantenimiento/detalle_vehiculo.html', {
        'vehiculo': vehiculo,
        'mantenimientos': mantenimientos,
        'costo_total': costo_total
    })

def lista_mantenimientos(request):
    mantenimientos = Mantenimiento.objects.all().order_by('-fecha')
    
    # Búsqueda
    query = request.GET.get('q')
    if query:
        mantenimientos = mantenimientos.filter(
            Q(vehiculo__placa__icontains=query) |
            Q(vehiculo__marca__icontains=query) |
            Q(descripcion__icontains=query)
        )
    
    # Filtro por estado
    estado = request.GET.get('estado')
    if estado == 'pendientes':
        mantenimientos = mantenimientos.filter(completado=False)
    elif estado == 'completados':
        mantenimientos = mantenimientos.filter(completado=True)
    
    return render(request, 'mantenimiento/lista_mantenimientos.html', {
        'mantenimientos': mantenimientos,
        'query': query,
        'estado': estado
    })

def dashboard(request):
    total_vehiculos = Vehiculo.objects.count()
    mantenimientos_pendientes = Mantenimiento.objects.filter(completado=False).count()
    mantenimientos_completados = Mantenimiento.objects.filter(completado=True).count()
    
    return render(request, 'mantenimiento/dashboard.html', {
        'total_vehiculos': total_vehiculos,
        'mantenimientos_pendientes': mantenimientos_pendientes,
        'mantenimientos_completados': mantenimientos_completados,
    })

# VISTAS PARA FORMULARIOS

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            placa = form.cleaned_data['placa']
            # Verificar si ya existe
            vehiculo_existente = Vehiculo.objects.filter(placa=placa).first()
            if vehiculo_existente:
                messages.info(request, f'El vehículo con placa {placa} ya existe en el sistema.')
                return redirect('mantenimiento:detalle_vehiculo', vehiculo_id=vehiculo_existente.id)
            else:
                vehiculo = form.save()
                messages.success(request, f'Vehículo {vehiculo.placa} agregado exitosamente.')
                return redirect('mantenimiento:lista_vehiculos')
    else:
        form = VehiculoForm()
    
    # Obtener todos los vehículos existentes para el selector
    vehiculos_existentes = Vehiculo.objects.all().order_by('placa')
    
    return render(request, 'mantenimiento/agregar_vehiculo.html', {
        'form': form,
        'vehiculos_existentes': vehiculos_existentes
    })

def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, f'Vehículo {vehiculo.placa} actualizado exitosamente.')
            return redirect('mantenimiento:detalle_vehiculo', vehiculo_id=vehiculo.id)
    else:
        form = VehiculoForm(instance=vehiculo)
    
    return render(request, 'mantenimiento/editar_vehiculo.html', {
        'form': form,
        'vehiculo': vehiculo
    })

def agregar_mantenimiento(request, vehiculo_id=None):
    vehiculo = None
    if vehiculo_id:
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    
    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            mantenimiento = form.save()
            messages.success(request, 'Mantenimiento registrado exitosamente.')
            return redirect('mantenimiento:detalle_vehiculo', vehiculo_id=mantenimiento.vehiculo.id)
    else:
        form = MantenimientoForm()
        if vehiculo:
            form.fields['vehiculo'].initial = vehiculo
    
    return render(request, 'mantenimiento/agregar_mantenimiento.html', {
        'form': form,
        'vehiculo': vehiculo
    })

def editar_mantenimiento(request, mantenimiento_id):
    mantenimiento = get_object_or_404(Mantenimiento, id=mantenimiento_id)
    
    if request.method == 'POST':
        form = MantenimientoForm(request.POST, instance=mantenimiento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mantenimiento actualizado exitosamente.')
            return redirect('mantenimiento:detalle_vehiculo', vehiculo_id=mantenimiento.vehiculo.id)
    else:
        form = MantenimientoForm(instance=mantenimiento)
    
    return render(request, 'mantenimiento/editar_mantenimiento.html', {
        'form': form,
        'mantenimiento': mantenimiento
    })