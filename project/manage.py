--- c:\projects\project\manage.py
+++ c:\projects\project\manage.py
@@ -1,158 +1,22 @@
+#!/usr/bin/env python
+"""Django's command-line utility for administrative tasks."""
+import os
+import sys
 
-+"""Django's command-line utility for administrative tasks."""
- import os
--from pathlib import Path
--
--# Build paths inside the project like this: BASE_DIR / 'subdir'.
--BASE_DIR = Path(__file__).resolve().parent.parent
-+import sys
- 
- 
--# Quick-start development settings - unsuitable for production
--# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
--
--# SECURITY WARNING: keep the secret key used in production secret!
--SECRET_KEY = 'django-insecure-!m)@@%p9)jqgl@azd5pd10f%#7a2#7gv2tbsk#*5$70z1zlg$n'
--
--# SECURITY WARNING: don't run with debug turned on in production!
--DEBUG = "True"
--
--ALLOWED_HOSTS = ['*']
-+def main():
-+    """Run administrative tasks."""
-+    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
-+    try:
-+        from django.core.management import execute_from_command_line
-+    except ImportError as exc:
-+        raise ImportError(
-+            "Couldn't import Django. Are you sure it's installed and "
-+            "available on your PYTHONPATH environment variable? Did you "
-+            "forget to activate a virtual environment?"
-+        ) from exc
-+    execute_from_command_line(sys.argv)
- 
- 
--# Application definition
--
--INSTALLED_APPS = [
--    'django.contrib.admin',
--    'django.contrib.auth',
--    'django.contrib.contenttypes',
--    'django.contrib.sessions',
--    'django.contrib.messages',
--    'django.contrib.staticfiles',
--    'rest_framework',
--    'corsheaders',
--    'credit',
--]
--
--MIDDLEWARE = [
--    'corsheaders.middleware.CorsMiddleware',
--    'django.middleware.security.SecurityMiddleware',
--    'django.contrib.sessions.middleware.SessionMiddleware',
--    'django.middleware.common.CommonMiddleware',
--    'django.middleware.csrf.CsrfViewMiddleware',
--    'django.contrib.auth.middleware.AuthenticationMiddleware',
--    'django.contrib.messages.middleware.MessageMiddleware',
--    'django.middleware.clickjacking.XFrameOptionsMiddleware',
--]
--
--ROOT_URLCONF = 'credit_approval_system.urls'
--
--TEMPLATES = [
--    {
--        'BACKEND': 'django.template.backends.django.DjangoTemplates',
--        'DIRS': [],
--        'APP_DIRS': True,
--        'OPTIONS': {
--            'context_processors': [
--                'django.template.context_processors.request',
--                'django.contrib.auth.context_processors.auth',
--                'django.contrib.messages.context_processors.messages',
--            ],
--        },
--    },
--]
--
--WSGI_APPLICATION = 'credit_approval_system.wsgi.application'
--
--
--# Database
--# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
--
--DATABASES = {
--    'default': {
--        'ENGINE': 'django.db.backends.postgresql',
--        'NAME': os.environ.get('PGDATABASE', 'postgres'),
--        'USER': os.environ.get('PGUSER', 'postgres'),
--        'PASSWORD': os.environ.get('PGPASSWORD', 'password'),
--        'HOST': os.environ.get('PGHOST', 'localhost'),
--        'PORT': os.environ.get('PGPORT', '5432'),
--    }
--}
--
--
--# Password validation
--# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
--
--AUTH_PASSWORD_VALIDATORS = [
--    {
--        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
--    },
--    {
--        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
--    },
--    {
--        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
--    },
--    {
--        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
--    },
--]
--
--
--# Internationalization
--# https://docs.djangoproject.com/en/5.2/topics/i18n/
--
--LANGUAGE_CODE = 'en-us'
--
--TIME_ZONE = 'UTC'
--
--USE_I18N = True
--
--USE_TZ = True
--
--
--# Static files (CSS, JavaScript, Images)
--# https://docs.djangoproject.com/en/5.2/howto/static-files/
--
--STATIC_URL = 'static/'
--STATIC_ROOT = BASE_DIR / 'staticfiles'
--
--# Default primary key field type
--# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
--
--DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
--
--# Django REST Framework
--REST_FRAMEWORK = {
--    'DEFAULT_RENDERER_CLASSES': [
--        'rest_framework.renderers.JSONRenderer',
--    ],
--    'DEFAULT_PARSER_CLASSES': [
--        'rest_framework.parsers.JSONParser',
--    ],
--}
--
--# CORS settings
--CORS_ALLOW_ALL_ORIGINS = True
--
--# Celery Configuration
--CELERY_BROKER_URL = 'redis://localhost:6379/0'
--CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
--CELERY_ACCEPT_CONTENT = ['json']
--CELERY_TASK_SERIALIZER = 'json'
--CELERY_RESULT_SERIALIZER = 'json'
--CELERY_TIMEZONE = TIME_ZONE
-+if __name__ == '__main__':
-+    main()
+
+def main():
+    """Run administrative tasks."""
+    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
+    try:
+        from django.core.management import execute_from_command_line
+    except ImportError as exc:
+        raise ImportError(
+            "Couldn't import Django. Are you sure it's installed and "
+            "available on your PYTHONPATH environment variable? Did you "
+            "forget to activate a virtual environment?"
+        ) from exc
+    execute_from_command_line(sys.argv)
+
+
+if __name__ == '__main__':
+    main()