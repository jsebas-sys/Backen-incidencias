# helpdesk_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta del panel de administración
    path('incidencias/', include('incidencias.urls')),  # Incluye las rutas de la app incidencias
]
