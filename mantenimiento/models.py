from django.db import models

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    kilometraje = models.IntegerField(default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"

class Mantenimiento(models.Model):
    TIPO_CHOICES = [
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
        ('emergencia', 'Emergencia'),
    ]
    
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    fecha = models.DateField()
    kilometraje_actual = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    taller = models.CharField(max_length=100)
    completado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.vehiculo} - {self.tipo} ({self.fecha})"