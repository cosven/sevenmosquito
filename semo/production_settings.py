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
        'PASSWORD': '123456',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}
