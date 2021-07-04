"""
Django settings for task project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3#t(q@(h5sif1(4gb91#j=*16yh&1%ryt2)i69@&ud=6donq%$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

ADMINS = (('Sadashiv', 'sadamsrit@gmail.com'))
SERVER_EMAIL = 'donotreply@gmail.com'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usermgmt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

ROOT_URLCONF = 'task.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        #'DIRS': [],
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

WSGI_APPLICATION = 'task.wsgi.application'

#Logut user after login time reaches 5minutes
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 1800
SESSION_IDLE_TIMEOUT = 5
SESSION_SAVE_EVERY_REQUEST = True

#SESSION_SECURITY_WARN_AFTER = 1 # Default 540
#SESSION_SECURITY_EXPIRE_AFTER = 1 # Default 600
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True


#Middleware
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
#X_FRAME_OPTIONS  = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False

#USE_THOUSAND_SEPARATOR = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


#STATICFILES_DIRS = (
#    STATIC_PATH,
#)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


REGISTRATION_OPEN = True # If true user can register
ACCOUNT_ACTIVATION_DAYS = 7 # One week activation windows
REGISTRATION_AUTO_LOGIN = True # If True the user will be automatically logged in
LOGIN_URL='login'
LOGIN_REDIRECT_URL = '/index'

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sadamsrit@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = False
#This did the trick
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DEFAULT_AUTO_FIELD='django.db.models.AutoField'
