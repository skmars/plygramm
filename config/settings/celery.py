from config.env import env

# https://docs.celeryproject.org/en/stable/userguide/configuration.html

CELERY_BROKER_URL = env("redis://localhost:6379")
CELERY_RESULT_BACKEND = "redis://localhost:6379"

CELERY_ACCEPT_CONTENT = ["application/json"]

CELERY_TIMEZONE = "UTC"

CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TASK_SOFT_TIME_LIMIT = 20  # seconds
CELERY_TASK_TIME_LIMIT = 30  # seconds
CELERY_TASK_MAX_RETRIES = 3
