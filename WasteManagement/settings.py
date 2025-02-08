
import os

PORT = os.environ.get("PORT", 8000)  # Default to 8000 if PORT is not set

# from pathlib import Path

# Add these at the top of your settings.py
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse

load_dotenv()

# Replace the DATABASES section of your settings.py with this
tmpPostgres = urlparse(os.getenv("postgresql://neondb_owner:npg_JEFIGb4L3rhP@ep-aged-dawn-a1sfnikw-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"))


BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2s2hkz86bf7pc6_n+t-jqa7+mkqny3h)syt2n*7%-fm8$)p!m5'
DEBUG = True
ALLOWED_HOSTS = ['*']

# 8th Feb
# SECRET_KEY = os.getenv('django-insecure-2s2hkz86bf7pc6_n+t-jqa7+mkqny3h)syt2n*7%-fm8$)p!m5', 'fallback-secret-key')
# DEBUG = os.getenv('DEBUG') == 'True'
# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Security
# SECRET_KEY = os.getenv('django-insecure-2s2hkz86bf7pc6_n+t-jqa7+mkqny3h)syt2n*7%-fm8$)p!m5', 'fallback-secret-key')
# DEBUG = os.getenv('DEBUG', 'True') == 'True'
# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
# # Database
# DATABASES = {
#     'default': dj_database_url.config(default=os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/mydatabase'))
# }

AUTH_USER_MODEL = 'waste.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'waste',
    'admin_app',
    'csp',
    'waste.apps.WasteConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'csp.middleware.CSPMiddleware',
    
]

ROOT_URLCONF = 'WasteManagement.urls'

TEMPLATES = [
    {
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
    },
]

WSGI_APPLICATION = 'WasteManagement.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'waste_management',
#         'USER': 'waste_user',
#         'PASSWORD': 'securepassword',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': tmpPostgres.path.replace('/', ''),
        'NAME': tmpPostgres.path.decode().replace('/', ''),
        'USER': tmpPostgres.username,
        'PASSWORD': tmpPostgres.password,
        'HOST': tmpPostgres.hostname,
        'PORT': 5432,
    }
}



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

# Add this if you want to serve static files from a custom folder
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
LOGIN_URL = '/login/'  # Change this to match your login URL pattern
AUTH_USER_MODEL = 'waste.CustomUser'
LOGIN_REDIRECT_URL = '/upload-photo/' 
LOGOUT_REDIRECT_URL = '/'  # Redirect to homepage after logout

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# CSP_DEFAULT_SRC = ("'self'",)  # Default policy to restrict to self
# CSP_SCRIPT_SRC = ("'self'", "'nonce-{nonce}'")

# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'",)  # Allow inline scripts
# CSP_STYLE_SRC = ("'self'", "'unsafe-inline'",)  # Allow inline styles
# CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://getbootstrap.com/")  # Allow inline styles

# CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", "https://unpkg.com")  # Example of allowing external JS resources

# settings.py

# Define the Content Security Policy
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_STYLE_SRC = ("'self'", "https://stackpath.bootstrapcdn.com", "https://cdnjs.cloudflare.com", "https://fonts.googleapis.com")
# CSP_SCRIPT_SRC = ("'self'", "https://code.jquery.com", "https://stackpath.bootstrapcdn.com", "https://cdn.jsdelivr.net", "https://cdnjs.cloudflare.com")
# CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com")
# CSP_IMG_SRC = ("'self'", "data:", "https://*")  # Allow images from any source, including inline images (data: URIs)

# CSP_INCLUDE_NONCES_IN = ["script-src", "style-src"]  # Use nonces for inline script and style execution
