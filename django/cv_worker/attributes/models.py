import uuid
from django.db import models

class Attribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    scanner = models.ForeignKey('scanners.Scanner', on_delete=models.CASCADE, null=True)
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, null=True)
    operation = models.ForeignKey('operations.Operation', on_delete=models.CASCADE, null=True)
    other_source_type = models.CharField(max_length=255)
    other_source_id = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
