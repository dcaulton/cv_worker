import datetime
from rest_framework.response import Response
from rest_framework import viewsets
from cv_worker.tasks.models import Task
from cv_worker.attributes.models import Attribute
from cv_worker.operations.models import Operation

class TaskViewSet(viewsets.ViewSet):
    def list(self, request):
        tasks_list = Task.objects.all()
        return Response({"tasks": tasks_list})

    def list(self, request):
        tasks_dict = {}
        for task in Task.objects.all():
            task_obj = {
                'id': str(task.id),
                'operation': task.operation.name,
                'status': task.status,
                'created_on': datetime.datetime.strftime(task.created_on, '%Y-%m-%d %H:%M:%S'),
                'updated_on': datetime.datetime.strftime(task.updated_on, '%Y-%m-%d %H:%M:%S'),
            }

            attributes_list = []
            if Attribute.objects.filter(task=task).exists():
                for attribute in Attribute.objects.filter(task=task):
                    attr_obj = {
                        attribute.name: attribute.value,
                    }
                    attributes_list.append(attr_obj)
            task_obj['attributes'] = attributes_list

            tasks_dict[str(task.id)] = task_obj
        return Response({"tasks": tasks_dict})

    def create(self, request):
        requested_operation=request.data['operation'],
        # TODO shouldn't need to index to 0 here, what's up?
        if not Operation.objects.filter(name=requested_operation[0]).exists():
            return Response('requesting a task for an unsupported operation', status=400)
        operation = Operation.objects.filter(name=requested_operation[0]).first()
        task = Task(
            operation=operation,
            status='created',
            request_data=request.data.get('request_data'),
        )
        task.save()

        if request.data.get('job_update_url'):
            attribute = Attribute(
                task=task,
                name='job_update_url',
                value=request.data.get('job_update_url')
            )
            attribute.save()

        return Response({'task_id': task.id})
