from .base import *
from decouple import config

DEBUG = False

ADMINS = [
    ("admin admin", "admin@email.com"),
]

ALLOWED_HOSTS = ["educaproject.com", "www.educaproject.com"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB", default="postgres"),
        "USER": config("POSTGRES_USER", default="postgres"),
        "PASSWORD": config("POSTGRES_PASSWORD", default="postgres"),
        "HOST": "db",
        "PORT": 5432,
    }
}

REDIS_URL = "redis://cache:6379"
CACHES["default"]["LOCATION"] = REDIS_URL
CHANNEL_LAYERS["default"]["CONFIG"]["hosts"] = [REDIS_URL]
