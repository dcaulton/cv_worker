import datetime
import json
from django.conf import settings
import requests
from rest_framework.response import Response
from rest_framework import viewsets, status
from cv_worker.operations.models import Operation
from cv_worker.attributes.models import Attribute

class OperationViewSet(viewsets.ViewSet):
    def list(self, request):
        operations_dict = {}
        for operation in Operation.objects.all():
            oper_obj = {
                'id': str(operation.id),
                'name': operation.name,
                'description': operation.description,
                'status': operation.status,
                'created_on': datetime.datetime.strftime(operation.created_on, '%Y-%m-%d %H:%M:%S'),
                'updated_on': datetime.datetime.strftime(operation.updated_on, '%Y-%m-%d %H:%M:%S'),
            }

            attributes = {}
            if Attribute.objects.filter(operation=operation).exists():
                for attribute in Attribute.objects.filter(operation=operation):
                    attributes[attribute.name] = attribute.value
            oper_obj['attributes'] = attributes

            operations_dict[operation.name] = oper_obj
        return Response({"operations": operations_dict})

    def retrieve(self, request, pk):
        if not Operation.objects.filter(pk=pk).exists():
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        operation = Operation.objects.get(pk=pk)
        oper_obj = {
            'id': str(operation.id),
            'name': operation.name,
            'description': operation.description,
            'status': operation.status,
            'created_on': datetime.datetime.strftime(operation.created_on, '%Y-%m-%d %H:%M:%S'),
            'updated_on': datetime.datetime.strftime(operation.updated_on, '%Y-%m-%d %H:%M:%S'),
        }

        if Attribute.objects.filter(operation=operation).exists():
            attributes = {}
            for attribute in Attribute.objects.filter(operation=operation):
                attributes[attribute.name] = attribute.value
        oper_obj['attributes'] = attr_obj

        return Response({"operation": oper_obj})

    def delete(self, request, pk, format=None):
        operation = Operation.objects.get(pk=pk)
        operation.delete()
        return Response('', status=204)

class OperationLookForWorkViewSet(viewsets.ViewSet):
    def create(self, request):
        url_to_hit = ''
        if not request.data.get('message_format'):
            return self.error('message_format is required')
        if (request.data.get('message_format') == 'gr_job' and
                not request.data.get('remote_base_url')):
            return self.error('remote_base_url is required')
        if request.data.get('message_format') == 'gr_job':
            url_to_hit = request.data.get('remote_base_url') + '?pick-up-for=' + settings.WORKER_POOL_ID
        jobs_response = requests.get(url_to_hit)
        if jobs_response.status_code != 200:
            print(jobs_response.content)
            return Response('BAD RESPONSE WHILE LOOKING FOR WORK', status=400)
        json_resp = json.loads(jobs_response.content)
        if len(json_resp['jobs']) > 0:
            print('found a job, taking it')
            job_url = request.data.get('remote_base_url') + '/' + json_resp['jobs'][0]['id']
            job_response = requests.get(job_url)
            if job_response.status_code != 200:
                print(job_response.content)
                return Response('BAD RESPONSE WHILE GETTING ONE WORK ITEM', status=400)
            json_resp = json.loads(jobs_response.content)
            print(json_resp)
            # TODO dispatch this as a task next
            return Response(json_resp)
        return Response()
