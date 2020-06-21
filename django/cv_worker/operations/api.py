import datetime
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

            attributes_list = []
            if Attribute.objects.filter(operation=operation).exists():
                for attribute in Attribute.objects.filter(operation=operation):
                    attr_obj = {
                        'name': attribute.name,
                        'value': attribute.value,
                    }
                    attributes.append(attr_obj)
            oper_obj['attributes'] = attributes_list

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
            attributes = []
            for attribute in Attribute.objects.filter(operation=operation):
                attr_obj = {
                    'name': attribute.name,
                    'value': attribute.value,
                }
                attributes.append(attr_obj)
        oper_obj['attributes'] = attr_obj

        return Response({"operation": oper_obj})

