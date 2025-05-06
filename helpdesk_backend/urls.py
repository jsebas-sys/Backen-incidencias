from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración
    path('api/incidencias/', include('incidencias.urls')),  # Ruta para la API de incidencias
]
