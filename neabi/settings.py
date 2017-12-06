"""
Django settings for neabi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c=1y@c46jhvuys*#entn4veitucyf-s&ta8bgt)s*mzhw*yg#9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

DJANGO_APPS = (
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

EXTERNAL_APPS = (
    'django_comments',
    'mptt',
    'zinnia_bootstrap',
    'sorl.thumbnail',
    'tagging',
    'tinymce',
    'zinnia',
    'zinnia_tinymce',
    'django_nose',
    'bootstrap3',
    'bootstrap_pagination',
    'watson',
    'hamlpy',
)

LOCAL_APPS = (
    'core.apps.CoreConfig',
)

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'neabi.urls'

WSGI_APPLICATION = 'neabi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_files'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# TEMPLATE_LOADERS = (
#     'app_namespace.Loader',
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
#     'hamlpy.template.loaders.HamlPyFilesystemLoader',
#     'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
# )

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'templates/'),
# )

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.contrib.messages.context_processors.messages',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.request',
#     'django.core.context_processors.media',
#     'django.core.context_processors.static',
#     'zinnia.context_processors.version',
#     'core.context_processors.social',
#     'core.context_processors.destaque_acervo',
# )


TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'zinnia.context_processors.version',
                'core.context_processors.social',
                'core.context_processors.destaque_acervo',
            ],
            'loaders':[
                'hamlpy.template.loaders.HamlPyFilesystemLoader',
                'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
                'app_namespace.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ]
        },
    }]



BOOTSTRAP3 = {
    'jquery_url': os.path.join(STATIC_URL, 'js/jquery-1.11.1.min.js'),
    'css_url': os.path.join(STATIC_URL, 'bootstrap3/css/bootstrap.min.css'),
    'javascript_url': os.path.join(STATIC_URL, 'bootstrap3/js/bootstrap.min.js'),
    'horizontal_label_class': 'col-md-2',
    'horizontal_field_class': 'col-md-10',
}


TINYMCE_FILEBROWSER = True

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'mobile': {'theme': 'mobile'},
    'mode': "textareas",
    'plugins': "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,advlist,autosave",

    'theme_advanced_buttons1': "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect,|,code",
    'theme_advanced_buttons2': "cut,copy,paste,pastetext,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,forecolor,backcolor",
    'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,advhr,|,ltr,rtl",

    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': "true",

    'theme_advanced_buttons1_add': "media",
    'theme_advanced_buttons2_add': "advimage",

    'language': "{{ language }}",
    'directionality': "{{ directionality }}",
    'spellchecker_languages': "{{ spellchecker_languages }}",
    'spellchecker_rpc_url': "{{ spellchecker_rpc_url }}",

}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-spec',
    '--spec-color',
    '--nologcapture',
    '--verbosity=1',
]
