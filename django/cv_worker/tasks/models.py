import uuid
from django.db import models

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operation = models.ForeignKey('operations.Operation', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=36)
    description = models.CharField(max_length=255)
    request_data = models.TextField(null=True)
    response_data = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
