from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
load_dotenv()                                           # Загружаем переменные из файла, после чего
SECRET_KEY = os.environ.get('SECRET_KEY', 'SecretKey')  # получаем значение секретного ключа
DEBUG = os.environ.get('DEBUG', False)                  # и DEBUG

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tasks"                                             # Регистрируем приложение
]

# Промежуточный слой ПО для обработки запросов и ответов
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Основной файл url-сопоставления
ROOT_URLCONF = "ToDo3.urls"

# Шаблоны
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],  # Задаём папку для шаблонов аутентификации
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ToDo3.wsgi.application"


# Database
DATABASES = {
    "default": {                                    # Задаём параметры для подключения к MySQL
        "ENGINE": "django.db.backends.mysql",       
        "NAME": os.environ['NAME'],                 # Получаем значения параметров из файла .env
        "USER": os.environ['USER'],
        "PASSWORD": os.environ['PASSWORD'],         
        "HOST": os.environ['HOST'],
        "PORT": "3306",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            "charset": "utf8mb4"
        }
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "ru-Ru"                                 # Задаём русский язык
TIME_ZONE = "Europe/Samara"                             # Задаём свою временную зону
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Перенаправление на страницу после входа 
LOGIN_REDIRECT_URL = '/tasks/'                          
