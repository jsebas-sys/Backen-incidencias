from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncidenciaViewSet

# Creamos el router y registramos el viewset
router = DefaultRouter()
router.register(r'incidencias', IncidenciaViewSet)

# Incluimos las rutas en la app
urlpatterns = [
    path('api/', include(router.urls)),  # Final: /incidencias/api/incidencias/
]
