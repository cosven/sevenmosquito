"""
override configurations in settings
"""

from .settings import *  # noqa


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'semo',
        'USER': 'root',
        'PASSWORD': '',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}
