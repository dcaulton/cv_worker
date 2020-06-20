import uuid
import datetime
from django.db import models

class Operation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        ret_obj = {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'created_on': datetime.datetime.strftime(self.created_on, '%Y-%m-%d %H:%M:%S'),
            'updated_on': datetime.datetime.strftime(self.updated_on, '%Y-%m-%d %H:%M:%S'),
        }
        return ret_obj
