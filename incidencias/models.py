from django.db import models
from django.contrib.auth.models import User

class Incidencia(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('resuelto', 'Resuelto'),
    ]
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]

    codigo = models.CharField(max_length=10)
    equipo = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='media')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    detalle = models.TextField()

    def __str__(self):
        return f"{self.codigo} - {self.estado}"
