import os


PROJECT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), )
TEST_SETUP_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '../../', 'test_setup' )

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TEST_SETUP_DIR, 'testdb' , 'miniverse_db1.sqlite3'),
    }
}

TIME_ZONE =  'America/New_York'

SECRET_KEY = 'o$qugz7!d7=l=qm7=*74jcp0ewudl*-povd=w2x^@3$rw*(qa7'

ROOT_URLCONF = 'miniverse.urls_test'

SITE_ID = 1

LOGIN_URL = 'admin:index'

SESSION_COOKIE_NAME = 'miniverse_dev'

# Used for working with GIS files
#   example: extracting shapefiles
# Needs to be writable by application
# Cleaned out by cron job
#
MEDIA_ROOT = os.path.join(TEST_SETUP_DIR, 'media_root' )
MEDIA_URL = '/media/'

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, "static") ,)  # original file source
STATIC_ROOT = os.path.join(TEST_SETUP_DIR, 'static_root') # where files gathered and served from
STATIC_URL = '/static/' # url for static files

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    
    'dataverse',
    'dataset',
    'metadata',
    'mock_token',

)
