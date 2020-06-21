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

    for i in range(10):
        percent_done = i * 10
        time.sleep(1)
        task.update_percent_complete(percent_done)
        task.save()

    task.update_message('we are finishing up my friend')
    task.save()

    resp_obj = {
        'message': 'flippity bippity',
    }
    task.response_data = json.dumps(resp_obj)
    task.status = 'success'
    task.save()


