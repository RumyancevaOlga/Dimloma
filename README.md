# Интернет-магазин 
### Проект представляет собой макет интернет-магазина по продоже электронных схем для вышивки крестом с реализованной системой авторизации и регистрации пользователей.
Для того, чтобы запустить проект на локальном компьютере необходимо скачать его на свой компьютер, заменить содержимое файла settings.py на
    
    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent.parent
  
    SECRET_KEY = '*******'

    DEBUG = True

    ALLOWED_HOSTS = [
    ]

    INSTALLED_APPS = [
      'online_store',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
    ]

    MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'website.urls'

    TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
    ]

    WSGI_APPLICATION = 'website.wsgi.application'

    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
    }
  
    AUTH_PASSWORD_VALIDATORS = [
      {
          'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
      },
    ]

    LANGUAGE_CODE = 'ru-ru'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_TZ = True

    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'static/'

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    MEDIA_ROOT = BASE_DIR / 'media'

    MEDIA_URL = '/media/'

Далее необходимо настроить виртуальное окружение, установив в него все библиотеки из файла requerements.txt.

Запускаем как стандартный проект Django.

Развернутый проект доступен по ссылке https://crossstitch.pythonanywhere.com/
