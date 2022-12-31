from .base import *  # noqa

"""
https://cheat.readthedocs.io/en/latest/django/celery.html
"""
CELERY_BROKER_BACKEND = "memory"
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
