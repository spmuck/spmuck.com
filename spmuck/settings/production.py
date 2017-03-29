from __future__ import absolute_import, unicode_literals

from .base import *

from .secrets import *

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# you must implement secrets.py in same folder for DB info
DATABASES = {
    'default': {
        'ENGINE': SECRET_DB_ENGINE,
        'NAME': SECRET_DB_NAME,
        'USER': SECRET_DB_USER,
        'PASSWORD': SECRET_DB_PASSWORD,
        'HOST': SECRET_DB_HOST,
        'PORT': SECRET_DB_PORT,
    }
}

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
