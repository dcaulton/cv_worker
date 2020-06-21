import json
import uuid
import requests
from django.db import models
from cv_worker.attributes.models import Attribute

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operation = models.ForeignKey('operations.Operation', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=36)
    description = models.CharField(max_length=255)
    request_data = models.TextField(null=True)
    response_data = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def finish_successfully(self, response_object):
        self.response_data = json.dumps(response_object)
        self.status = 'success'
        self.save()

        update_url = self.get_job_update_url()
        if update_url:
            payload = {
                'percent_complete': 1,
                'status': 'success',
                'response_data': self.response_data,
            }
            response = requests.patch(
                update_url,
                data=payload,
            )
            print('closing out remote parent job')
            if response.status_code != 200:
                print('remote job close faied with url {}'.format(update_url))
                print('remote job close faied with status {}'.format(response.status_code))
                print('remote job close content {}'.format(response.content))

    def update_percent_complete(self, percent_complete):
        if Attribute.objects.filter(task=self).filter(name='percent_complete').exists():
            attribute = Attribute.objects.filter(task=self).filter(name='percent_complete').first()
            attribute.percent_complete = percent_complete
            attribute.save()
        else:
            attribute = Attribute(
                name='percent_complete',
                value=percent_complete,
            )
            attribute.save()

        update_url = self.get_job_update_url()
        if update_url:
            payload = {
                'percent_complete': percent_complete,
            }
            if 0 < percent_complete < 1:
                payload['status'] = 'running'
            elif percent_complete == 1:
                payload['status'] = 'success'
            response = requests.patch(
                update_url,
                data=payload,
            )
            print('updating percent complete on remote parent job')
            if response.status_code != 200:
                print('remote job update faied with url {}'.format(update_url))
                print('remote job update faied with status {}'.format(response.status_code))
                print('remote job update content {}'.format(response.content))

    def get_job_update_url(self):
        if Attribute.objects.filter(task=self).filter(name='job_update_url').exists():
            return Attribute.objects.filter(task=self).filter(name='job_update_url').first().value

