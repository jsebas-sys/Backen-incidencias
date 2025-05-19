from rest_framework import serializers
from .models import Incidencia

class IncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidencia
        fields = ['id', 'codigo', 'equipo', 'fecha', 'estado', 'prioridad', 'usuario', 'detalle']
        read_only_fields = ['usuario']
