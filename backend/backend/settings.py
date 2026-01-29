"""
Django settings for backend project.
"""

import os
from pathlib import Path




# ---------------- BASE DIR & ENV ----------------
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------- SECURITY ----------------
SECRET_KEY = 'django-insecure-ueaj1recwi_e&8o5!jl*#o7323&kn64-l0m5=!423k+b^5n=d5'
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = []

# ---------------- APPLICATIONS ----------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# ---------------- DATABASE ----------------
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("MYSQLDATABASE"),
        "USER": os.environ.get("MYSQLUSER"),
        "PASSWORD": os.environ.get("MYSQLPASSWORD"),
        "HOST": os.environ.get("MYSQLHOST"),
        "PORT": os.environ.get("MYSQLPORT"),
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}



# ---------------- EMAIL ----------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")  # from .env
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")  # from .env
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ---------------- PASSWORD VALIDATION ----------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ---------------- INTERNATIONALIZATION ----------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------- STATIC & MEDIA ----------------
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ---------------- CORS ----------------


ALLOWED_HOSTS = [
    "deploye-test-backend.onrender.com",
    ".onrender.com",
    "localhost",
    "127.0.0.1",
]


CORS_ALLOWED_ORIGINS = [
    "https://citsfrontend.netlify.app",
]

CSRF_TRUSTED_ORIGINS = [
    "https://citsfrontend.netlify.app",
]



