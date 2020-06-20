from rest_framework.response import Response
from rest_framework import viewsets
from cv_worker.attributes.models import Attribute

class AttributeViewSet(viewsets.ViewSet):
    def list(self, request):
        attributes_list = Attribute.objects.all()
        return Response({"attributes": attributes_list})
