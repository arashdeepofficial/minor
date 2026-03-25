INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'users',
    'events',
    'registrations',
]

AUTH_USER_MODEL = 'users.User'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
