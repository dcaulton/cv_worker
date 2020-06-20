from rest_framework.response import Response
from rest_framework import viewsets
from cv_worker.tasks.models import Task

class TaskViewSet(viewsets.ViewSet):
    def list(self, request):
        tasks_list = Task.objects.all()
        return Response({"tasks": tasks_list})
