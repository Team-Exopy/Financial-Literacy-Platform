from datetime import timedelta
import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = []

# Set APPEND_SLASH to False to disable the automatic addition of trailing slashes to URLs. 
# By default, Django appends a trailing slash to URLs if the URL pattern does not match the request. 
# This behavior can cause problems, especially when dealing with URLs that end with a slash. 
# For example, a request for "/api/users/" would be redirected to "/api/users/?next=/api/users/", 
# which is not the intended behavior. 
# By setting APPEND_SLASH to False, we disable this automatic behavior and prevent such redirections.
APPEND_SLASH = False
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #self-created application 
    'api.apps.ApiConfig', # Using 'api.apps.ApiConfig' in INSTALLED_APPS is more flexible and allows you to customize the app's configuration and behavior.
    # third party application
    'rest_framework',
    'corsheaders', # Including 'corsheaders' in INSTALLED_APPS and configuring it properly is essential for enabling secure cross-origin requests
    'rest_framework_simplejwt.token_blacklist', # black_list refresh_acess_token so,it can't used any more
]

# Simple JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
# By setting 'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',) 
# in REST_FRAMEWORK, you ensure that all requests to your API endpoints are authenticated using JWT tokens.

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5), # When a user logs in, they receive an access token that is valid for a specific period, say 5 minutes.
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1), # When the access token expires after 1 days, the user can use the refresh token to get a new access token without logging in again.
    "ROTATE_REFRESH_TOKENS": True, # With ROTATE_REFRESH_TOKENS set to True, the user also gets a new refresh token with a renewed expiration
    "BLACKLIST_AFTER_ROTATION": True, # Enhances security by ensuring that old refresh tokens cannot be reused.
    "UPDATE_LAST_LOGIN": False, # Useful for tracking user logins but can increase the number of database transactions

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Corsheaders MiddleWare
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles') # Specifies the directory for collected static files during deployment.
STATIC_URL = '/static/' # Defines the URL for accessing static files.
MEDIA_URL = '/media/' # Defines the URL for accessing media files.
MEDIA_ROOT = os.path.join(BASE_DIR ,"media") # Specifies the directory for storing media files.
STATICFILES_DIRS = [ 
    BASE_DIR/'static', # Lists additional directories where Django will look for static files.
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS = True # Doesn't block any request . only used for development. remove if in deployment
CORS_ALLOW_CREDENTIALS = True

# Set the AUTH_USER_MODEL to use the custom User model defined in the 'api' app.
# This allows us to use the custom User model instead of the default Django User model.
# This is useful when you want to customize the user model or add additional fields.
AUTH_USER_MODEL = 'api.User' 

# Configure the REST framework settings.
# Set the default renderer class to our custom JSON renderer.
# This allows us to customize the JSON response format.
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        # Specify the fully qualified class name of the custom JSON renderer.
        # The custom JSON renderer is defined in the 'api' app.
        'api.renderers.CustomJSONRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 6,
     'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    # Set the default authentication class to JWTAuthentication.
    # This authentication class uses JWT (JSON Web Tokens) for authentication.
    # JWT tokens are used for stateless authentication and provide a secure way to authenticate requests.
    # The 'rest_framework_simplejwt.authentication.JWTAuthentication' class is used for this purpose.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
     'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '100/day',  # Limit each user to 100 requests per day
        'anon': '10/day',  # Limit each anonymous user to 10 requests per day
    }
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('PSWD')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'django': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': False,
    },
}
