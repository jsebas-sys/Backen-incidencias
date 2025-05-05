from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncidenciaViewSet

# Inicializamos el router
router = DefaultRouter()
# Registramos la vista IncidenciaViewSet con el prefijo 'incidencias'
router.register(r'incidencias', IncidenciaViewSet)

# Definimos las rutas que se manejarán en la aplicación
urlpatterns = [
    path('api/', include(router.urls)),  # Prefijo 'api/' para todas las rutas de la API
]
