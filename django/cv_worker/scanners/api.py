from rest_framework.response import Response
from rest_framework import viewsets
from cv_worker.scanners.models import Scanner

class ScannerViewSet(viewsets.ViewSet):
    def list(self, request):
        scanners_list = Scanner.objects.all()
        return Response({"scanners": scanners_list})
