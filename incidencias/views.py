from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, SAFE_METHODS, BasePermission
from .models import Incidencia
from .serializers import IncidenciaSerializer

class ReadOnlyOrAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated

class IncidenciaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar incidencias.
    Permite las operaciones CRUD sobre el modelo Incidencia.
    """
    queryset = Incidencia.objects.all()  
    serializer_class = IncidenciaSerializer  
    permission_classes = [ReadOnlyOrAuthenticated]  

    def perform_create(self, serializer):
        from django.contrib.auth.models import User
        default_user = User.objects.first()
        try:
            serializer.save(usuario=default_user)
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error saving incidencia: {e}")
            raise e

   