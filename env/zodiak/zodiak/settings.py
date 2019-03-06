
"""
Django settings for zodiak project.

Generated by 'django-admin startproject' using Django 1.8.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nmso-o2j6x4=w^sypv35=h6@5=npn5v18wz2_q*lcu0pn$2p^*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['isaiahiyede.pythonanywhere.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'zodiakApp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'zodiak.urls'

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

WSGI_APPLICATION = 'zodiak.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

LOGIN_REDIRECT_URL = '/accounts/login/'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'isaiahiyede$zodiak',
        'USER': 'isaiahiyede',
        'PASSWORD': 'ogheneyole@@101',
        'HOST': 'isaiahiyede.mysql.pythonanywhere-services.com',
    }
}


# DATABASES = {
#     'default': {
#     'NAME': 'zodiak_db',
#     'ENGINE': 'sqlserver_ado',
#     'HOST': '127.0.0.1',
#     'PORT': '1433',
#     'USER': 'Assetdb',
#     'PASSWORD': '1234567@gooGLE',
#     'OPTIONS': {
#             'provider': 'SQLNCLI11',
#             'use_legacy_date_fields': 'True'
#         }
#     }
# }


# DATABASES = {
#     'default': {
#     'NAME': 'zodiak_db',
#     'ENGINE': 'sqlserver_ado',
#     'HOST': '127.0.0.1',
#     'PORT': '1433',
#     'USER': 'Assetdb',
#     'PASSWORD': '1234567@gooGLE',
#     'OPTIONS': {
#             'provider': 'SQLNCLI11',
#             'use_legacy_date_fields': 'True'
#         }
#     }
# }


# DATABASES = {
#     'default': {
#     'NAME': 'zodiak_db',
#     'ENGINE': 'django.db.backends.mysql',
#     'HOST': '127.0.0.1',
#     'PORT': '3306',
#     'USER': 'root',
#     'PASSWORD': 'root',
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'zodiak_db',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = '/home/isaiahiyede/zodiak/env/zodiak/'
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# Additional locations of static files
STATICFILES_DIRS = (
    'static',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'
