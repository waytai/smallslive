from .local import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smallslive',
        'USER': 'boneill',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'old': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smallslive_old',
        'USER': 'boneill',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
