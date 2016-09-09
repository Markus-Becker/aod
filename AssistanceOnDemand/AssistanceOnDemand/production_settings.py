"""
Django settings for AssistanceOnDemand project.
"""

from os import path
from django.utils.translation import ugettext_lazy as _

PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# EVALUATION PROCESS
EVALUATION_PROCESS  = False
DEVELOPER_EMAIL = {developer_email}
RECEIVER_EMAIL = [{email}}] if EVALUATION_PROCESS == True else [DEVELOPER_EMAIL]

# AOD HOST INFO
AOD_HOST = {
    'PROTOCOL': "http",
    'IP': {public_ip}, 
    'PORT': {public_port},
    'PATH': {path}
}

PREVIEW_SITE_URL = AOD_HOST['PATH']

ALLOWED_HOSTS = (
    '*',
)

ADMINS = (
    ('takis', DEVELOPER_EMAIL),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pros4all',
        'USER': 'root',
        'PASSWORD': {password},
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#LOGIN_URL = '/login'
LOGIN_URL = '/callback/openam'


# OPENAM INTEGRATION
OPENAM_INTEGRATION = False
CLIENT_ID = {my_client_id}
CLIENT_SECRET = {my_client_secret}
OAUTH_SERVER = {authorization_server_ip}
REDIRECT_URL = AOD_HOST['PROTOCOL'] + "://" + AOD_HOST['IP'] + AOD_HOST['PATH'] + LOGIN_URL



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Athens'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGES = (
    ('el', _('Greek')),
    ('en', _('English')),
    ('it', _('Italian')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    ('de', _('German')),
)
LANGUAGE_CODE = 'en'
# cookie name for language
LANGUAGE_COOKIE_NAME = "aod_language"


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# MEDIA_ROOT = ''
MEDIA_ROOT = path.join(PROJECT_ROOT, 'media').replace('\\', '/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# MEDIA_URL = '/media/'
MEDIA_URL =  AOD_HOST['PATH'] + '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = path.join(PROJECT_ROOT, 'static').replace('\\', '/')

# URL prefix for static files.
#STATIC_URL = '/static/'
STATIC_URL = AOD_HOST['PATH'] + '/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # mine
    #"C:/Users/magni_000/Documents/Visual Studio 2013/Projects/AssistanceOnDemand/app/static"
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'n(bd1f1c%e8=_xad02x5qtfn%wgwpi492e$8_erx+d)!tpeoim'

# List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#    #'django.template.loaders.eggs.Loader',
#)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    # django debug tools
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.common.CommonMiddleware',    
)

ROOT_URLCONF = 'AssistanceOnDemand.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'AssistanceOnDemand.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'restapi',
    
    'django_extensions',

    # Debug toolbar
    'debug_toolbar',
    'django_dowser',

    # translation
    'rosetta',

    # Grappelli admin panel
    'grappelli',   
    'django.contrib.admin',
    'django.contrib.admindocs',
    'import_export',

    'rest_framework',
    'rest_framework_swagger',

    # analytics
    'analytical',

    # dynamic settings
    # 'constance',

    'corsheaders',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Specify the default test runner.
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# Settings for swagger
SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '1.0',
    'api_path': '/',
    'base_path': str(AOD_HOST['IP']) + ":" + str(AOD_HOST['PORT']) + str(AOD_HOST['PATH']) + '/docs',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete',
        'options'
    ],
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'unauthenticated_user': 'django.contrib.auth.models.AnonymousUser',
    #'permission_denied_handler': None,
    #'resource_access_handler': None,
    'info': {
        'contact': DEVELOPER_EMAIL,
        'description': 'Find below the documentation of REST web services that AoD provides.',
        'license': 'Apache 2.0',
        'licenseUrl': 'http://www.apache.org/licenses/LICENSE-2.0.html',
        'title': 'Documentation of AoD web services',
    },
    'doc_expansion': 'none',
}



# Email account for notifications
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_USER     = {email_account}
EMAIL_HOST_PASSWORD = {email_account_password}
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True

# Django rest framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework_xml.parsers.XMLParser',
        'rest_framework_yaml.parsers.YAMLParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
        'rest_framework_yaml.renderers.YAMLRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50
}




GRAPPELLI_ADMIN_TITLE = "AoD administration panel"

# Grappelli template - admin panel
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ]  ,
        },
    },
]
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "admin_tools.template_loaders.TemplateLoader"
)


# django extensions
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}


# Django debug toolbar
#DEBUG_TOOLBAR_PANELS = (
#    'debug_toolbar.panels.version.VersionDebugPanel',
#    'debug_toolbar.panels.timer.TimerDebugPanel',
#    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#    'debug_toolbar.panels.headers.HeaderDebugPanel',
#    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
#    'debug_toolbar.panels.template.TemplateDebugPanel',
#    'debug_toolbar.panels.sql.SQLDebugPanel',
#    'debug_toolbar.panels.signals.SignalDebugPanel',
#    'debug_toolbar.panels.logger.LoggingPanel',
#)


# pip install pylibmc
#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:11211',
#    }
#}
#def get_cache():
#  import os
#  try:
#    os.environ['MEMCACHE_SERVERS'] = os.environ['MEMCACHIER_SERVERS'].replace(',', ';')
#    os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHIER_USERNAME']
#    os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHIER_PASSWORD']
#    return {
#      'default': {
#        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
#        'TIMEOUT': 500,
#        'BINARY': True,
#        'OPTIONS': { 'tcp_nodelay': True }
#      }
#    }
#  except:
#    return {
#      'default': {
#        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
#      }
#    }

#CACHES = get_cache()


LOCALE_PATHS = (
    path.join(PROJECT_ROOT, 'locale/'),
)

# Rosetta app
ROSETTA_MESSAGES_PER_PAGE = 32
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
#ROSETTA_ENABLE_REFLANG = True

# CONSTANCE app
#CONSTANCE_CONFIG = {
#    'THE_ANSWER': (42, 'Answer to the Ultimate Question of Life, '
#                       'The Universe, and Everything'),
#}
#CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True

# Google analytics
GOOGLE_ANALYTICS_PROPERTY_ID = {google_key}
ANALYTICAL_INTERNAL_IPS = [{list_of_IPs}]
ANALYTICAL_AUTO_IDENTIFY = False
GOOGLE_ANALYTICS_DISPLAY_ADVERTISING = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)