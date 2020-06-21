import datetime
from rest_framework.response import Response
from rest_framework import viewsets, status
from cv_worker.tasks.models import Task
from cv_worker.attributes.models import Attribute
from cv_worker.operations.models import Operation
from cv_worker.tasks import celery_tasks

def dispatch_task(task):
    if task.operation.name == 'ping_cv_worker':
        celery_tasks.ping_cv_worker.delay(task.id)
    else:
        print('unrecognized operation *{}* for task {}'.format(task.operation.name, task.id))

class TaskViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk):
        if not Task.objects.filter(pk=pk).exists():
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        task = Task.objects.get(pk=pk)
        operation_name = ''
        if task.operation:
            operation_name = task.operation.name
        task_obj = {
            'id': str(task.id),
            'operation': operation_name,
            'status': task.status,
            'request_data': task.request_data,
            'response_data': task.response_data,
            'created_on': datetime.datetime.strftime(task.created_on, '%Y-%m-%d %H:%M:%S'),
            'updated_on': datetime.datetime.strftime(task.updated_on, '%Y-%m-%d %H:%M:%S'),
        }

        if Attribute.objects.filter(task=task).exists():
            attributes = {}
            for attribute in Attribute.objects.filter(task=task):
                attributes[attribute.name] = attribute.value
        task_obj['attributes'] = attributes

        return Response({"task": task_obj})


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

            attributes = {}
            if Attribute.objects.filter(task=task).exists():
                for attribute in Attribute.objects.filter(task=task):
                    attributes[attribute.name] = attribute.value
            task_obj['attributes'] = attributes

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

        dispatch_task(task)

        return Response({'task_id': task.id})

    def delete(self, request, pk, format=None):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response('', status=204)

