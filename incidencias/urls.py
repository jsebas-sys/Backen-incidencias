from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncidenciaViewSet

router = DefaultRouter()
router.register(r'incidencias', IncidenciaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Esto da /api/incidencias/
]
