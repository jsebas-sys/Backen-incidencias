import os
from pathlib import Path
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key & debug
SECRET_KEY = config('SECRET_KEY', default='django-insecure-secret-key')
DEBUG = config('DEBUG', cast=bool, default=False)

# Hosts permitidos (mejor usar variable de entorno en producción)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

# Apps instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'incidencias',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Asegúrate de tener este middleware activado
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'helpdesk_backend.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

WSGI_APPLICATION = 'helpdesk_backend.wsgi.application'

# Base de datos
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# Validadores de contraseña (puedes añadir más en producción)
AUTH_PASSWORD_VALIDATORS = []

# Configuración regional
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS
CORS_ALLOW_ALL_ORIGINS = True  # Si deseas permitir todos los orígenes
CORS_ALLOW_CREDENTIALS = True  # Si también necesitas permitir cookies y autenticación
CSRF_TRUSTED_ORIGINS = [
    'https://backen-incidencias-production.up.railway.app',  # Asegúrate de agregar tu dominio aquí
    # Agrega cualquier otro dominio confiable que necesites
]

