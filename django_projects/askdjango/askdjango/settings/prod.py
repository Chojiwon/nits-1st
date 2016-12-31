import os
from .common import * 

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, "..", "staticfiles")

MEDIA_ROOT = os.path.join(BASE_DIR, "..", "media")

DATABASES = {
    'default': { 
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nits',
        'USER': 'nits',
        'PASSWORD': 'withaskdjango!',
        'HOST': '127.0.0.1',
    },
}

