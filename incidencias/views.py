from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Incidencia
from .serializers import IncidenciaSerializer

class IncidenciaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar incidencias.
    Permite las operaciones CRUD sobre el modelo Incidencia.
    """
    queryset = Incidencia.objects.all()  
    serializer_class = IncidenciaSerializer  
    permission_classes = [IsAuthenticated]  

   