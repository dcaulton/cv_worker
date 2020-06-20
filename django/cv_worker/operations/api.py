from rest_framework.response import Response
from rest_framework import viewsets
from cv_worker.operations.models import Operation

class OperationViewSet(viewsets.ViewSet):
    def list(self, request):
        operations_list = []
        for operation in Operation.objects.all():
            operations_list = operation.__str__()
        return Response({"operations": operations_list})
