# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.realpath(os.path.dirname(os.path.realpath(__file__)))
SECRET_KEY = 'ff' * 30
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = ('hayes_test',)
MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.request',
	"django.core.context_processors.csrf",
	"hayes_test.settings.extra_context",
	"django.contrib.messages.context_processors.messages"
)
ROOT_URLCONF = 'hayes_test.app'
WSGI_APPLICATION = 'hayes_test.app.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}}
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
TEMPLATE_LOADERS = ('coffin.contrib.loader.AppLoader', 'coffin.contrib.loader.FileSystemLoader',)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False
TEMPLATE_DIRS = [BASE_DIR]

HAYES_INDEXES = [
	"hayes_test.index:get_indexes",
]
HAYES_SERVER = "http://localhost:9200/"
HAYES_DEFAULT_INDEX = "hh"

def extra_context(request):
	from django.conf import settings
	return {"settings": settings}
