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

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgi_redis.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('localhost', 6379)],
            },
        'ROUTING': 'askdjango.routing.channel_routing',
    },
}


import os
import raven

RAVEN_CONFIG = {
    # FIXME: 각자 설정에 맞춰 수정
    # https://docs.sentry.io/clients/python/integrations/django/
    'dsn': 'https://c1647f59f36e44f4833d5c6626695cd1:392001118d9d4e00b9dd0227bde8ede5@sentry.io/124899',
    # If you are using git, you can also automatically configure the release based on the git info.
    'release': 'askdjango',
}
