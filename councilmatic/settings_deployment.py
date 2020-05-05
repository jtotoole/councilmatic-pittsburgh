
# These are all the settings that are specific to a deployment

import os

# SECURITY WARNING: don't run with debug turned on in production!
# Set this to True while you are developing
DEBUG = os.getenv('DEBUG')

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'pittsburgh_councilmatic',
        'USER': '',
        'PASSWORD': '',
        'PORT': 5432,
    }
}

SECRET_KEY = os.getenv('SECRET_KEY')

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://localhost:8983/solr/councilmatic'
    },
}

# Remember to run python manage.py createcachetable so this will work!
# developers, set your BACKEND to 'django.core.cache.backends.dummy.DummyCache'
CACHES = {
    'default': {
        'BACKEND': os.getenv('BACKEND_DB_CACHE'),
        'LOCATION': 'councilmatic_cache',
    }
}

# Set this to flush the cache at /flush-cache/{FLUSH_KEY}
FLUSH_KEY = os.getenv('FLUSH_KEY')

# Set this to allow Disqus comments to render
DISQUS_SHORTNAME = None

# analytics tracking code
ANALYTICS_TRACKING_CODE = ''

# Google Maps API Key
GOOGLE_API_KEY = os.getenv('GOOGLE_MAPS_KEY')

HEADSHOT_PATH = os.path.join(os.path.dirname(__file__), '..'
                             '/pittsburgh/static/images/')

EXTRA_APPS = ()
