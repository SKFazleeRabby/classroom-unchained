from config.settings import *


DEBUG = False

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
