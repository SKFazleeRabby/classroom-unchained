from config.settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_ENGINE'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASS')
    }
}


INSTALLED_APPS += [
    'debug_toolbar',
    'template_debug'
]

MIDDLEWARE = [
     'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: not request.is_ajax() and request.META.get('HTTP_X_FORWARDED_FOR', None) in INTERNAL_IPS
}

