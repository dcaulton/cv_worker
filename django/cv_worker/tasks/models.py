import uuid
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

        if Attribute.objects.filter(task=self).filter(name='job_update_url').exists():
            # TODO update remote job if it exists
            print('SHOULD BE UPDATING THE REMOTE JOB PERCENT COMPLETE HERE')

    def update_message(self, message):
        if Attribute.objects.filter(task=self).filter(name='message').exists():
            attribute = Attribute.objects.filter(task=self).filter(name='message').first()
            attribute.message = message
            attribute.save()
        else:
            attribute = Attribute(
                name='message',
                value=message,
            )
            attribute.save()

        if Attribute.objects.filter(task=self).filter(name='job_update_url').exists():
            # TODO update remote job if it exists
            print('SHOULD BE UPDATING THE REMOTE JOB MESSAGE HERE')
