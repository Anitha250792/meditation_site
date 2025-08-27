import os
from pathlib import Path

# -------------------------------
# BASE CONFIG
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-secret-key")

# Debug
DEBUG = os.environ.get("DEBUG", "True") == "True"

# Allowed Hosts


# Allowed Hosts
ALLOWED_HOSTS = os.getenv(
    "DJANGO_ALLOWED_HOSTS",
    "127.0.0.1,localhost,meditation-site-2.onrender.com"
).split(",")



# -------------------------------
# APPLICATIONS
# -------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'widget_tweaks',
    'main',
]

# -------------------------------
# MIDDLEWARE
# -------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------
# URLS
# -------------------------------
ROOT_URLCONF = 'meditation_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "main" / "templates"],  # Your template folder
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

WSGI_APPLICATION = 'meditation_site.wsgi.application'

# -------------------------------
# DATABASE
# -------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------------
# PASSWORD VALIDATION
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# -------------------------------
# INTERNATIONALIZATION
# -------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# -------------------------------
# STATIC FILES (CSS, JS, Images)
# -------------------------------
STATIC_URL = '/static/'

# Local development static files
STATICFILES_DIRS = [BASE_DIR / "main" / "static"]

# Production static files
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -------------------------------
# MEDIA FILES (Optional)
# -------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# -------------------------------
# DEFAULT PRIMARY KEY
# -------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
