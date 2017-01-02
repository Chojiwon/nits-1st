# blog/tasks.py
import time
from celery import shared_task

@shared_task
def long_add(x, y):
    time.sleep(3)
    return x + y

