from celery import shared_task
import json
import time
from cv_worker.tasks.models import Task


@shared_task
def ping_cv_worker(task_id):
    print('yahoo, we are IN a real ping worker task')
    task = Task.objects.get(pk=task_id)
    task.status = 'running'
    task.save()

    for i in range(11):
        percent_done = i * .1
        time.sleep(5)
        task.update_percent_complete(percent_done)
        task.save()

    resp_obj = {
        'message': 'look at you, all solving problems and stuff',
    }

    task.finish_successfully(resp_obj)
