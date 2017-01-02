# blog/tasks.py
import json
import time
from celery import shared_task
from channels import Group

@shared_task
def long_add(x, y):
    time.sleep(3)
    return x + y


@shared_task
def task_using_websocket(user_http_session_key, start, end):
    name = 'session-{}'.format(user_http_session_key)
    group = Group(name)

    total = end - start
    for i in range(start, end):
        group.send({
            'text': json.dumps({
                'func': 'task_using_websocket',
                'status': 'message from task_using_websocket #{}'.format(i),
                'percent': 100*i/total,
            }),
        })
        time.sleep(0.3)

