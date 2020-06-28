from rest_framework.response import Response
from rest_framework import viewsets
from django.conf import settings
import json
import os
import shutil

class ServerSettingsViewSet(viewsets.ViewSet):
    def list(self, request):
        resp = settings.CV_WORKER
        return Response(resp)

    def patch(self, request, pk=None):
        if not request.data.get('CV_WORKER'):
            return Response('need cv worker top level tag', status=400)
        build_settings = {
            'CV_WORKER': settings.CV_WORKER,
        }
        for settings_key in request.data.get('CV_WORKER'):
            build_settings['CV_WORKER'][settings_key] = request.data.get('CV_WORKER')[settings_key]
     
        settings_filename = os.path.join(settings.BASE_DIR, 'server', 'settings.json')
        backup_settings_filename = os.path.join(settings.BASE_DIR, 'server', 'settings.json.bak')
        shutil.copyfile(settings_filename, backup_settings_filename)
        with open (settings_filename, 'w') as outfile:
            json.dump(build_settings, outfile, indent=2)

        return Response()
