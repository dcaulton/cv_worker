from rest_framework.response import Response
from rest_framework import viewsets
from cv_worker.operations.models import Operation

class OperationViewSet(viewsets.ViewSet):
    def list(self, request):
        operations_list = Operation.objects.all()
        return Response({"operations": operations_list})
