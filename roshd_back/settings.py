from datetime import timedelta
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iuohkgftyoiuhkyuiolkjbgj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authentication.apps.AuthenticationConfig',
    'projection.apps.ProjectionConfig',

    'rest_framework',
    'drf_spectacular',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

AUTH_USER_MODEL = 'authentication.User'
ROOT_URLCONF = 'roshd_back.urls'

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['projection/pdf_generator', ],
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

WSGI_APPLICATION = 'roshd_back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

_DEFAULT_TIME_RELATED_FORMAT = '%Y-%m-%d'
_DEFAULT_TIME_FORMAT = '%H-%M'

REST_FRAMEWORK = dict(
    DEFAULT_PERMISSION_CLASSES=('rest_framework.permissions.IsAuthenticated',),
    DEFAULT_AUTHENTICATION_CLASSES=(
        'rest_framework_simplejwt.authentication.JWTAuthentication',),
    UNAUTHENTICATED_USER=None,
    DEFAULT_RENDERER_CLASSES=('rest_framework.renderers.JSONRenderer',),
    DATE_FORMAT=_DEFAULT_TIME_RELATED_FORMAT,
    DATE_INPUT_FORMATS=[_DEFAULT_TIME_RELATED_FORMAT],
    # DATETIME_FORMAT=_DEFAULT_TIME_RELATED_FORMAT,
    # DATETIME_INPUT_FORMATS=[_DEFAULT_TIME_RELATED_FORMAT],
    TIME_FORMAT=_DEFAULT_TIME_FORMAT,
    TIME_INPUT_FORMATS=[_DEFAULT_TIME_FORMAT],
    DEFAULT_SCHEMA_CLASS='drf_spectacular.openapi.AutoSchema',
)

SIMPLE_JWT = dict(
    ACCESS_TOKEN_LIFETIME=timedelta(days=1),
    REFRESH_TOKEN_LIFETIME=timedelta(days=15),
    ROTATE_REFRESH_TOKENS=True,
    ALGORITHM='HS256',
    SIGNING_KEY=SECRET_KEY,
    AUTH_HEADER_TYPES=('Bearer',),
    USER_ID_FIELD='id',
    USER_ID_CLAIM='user_id',
)

SPECTACULAR_SETTINGS = {
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True,
        "docExpansion": None
    },
    "SWAGGER_UI_DIST": "//unpkg.com/swagger-ui-dist@3.42.0",
    'SCHEMA_PATH_PREFIX': r'/api/',
    'TITLE': 'Roshd API',
    'DESCRIPTION': 'Lorem ipsum.',
    'VERSION': '1.0.0',
}
