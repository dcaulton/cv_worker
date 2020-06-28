from django.contrib import admin
from django.urls import path
from django.urls import include
from .router import get_router
import cv_worker.attributes.urls
import cv_worker.scanners.urls
import cv_worker.tasks.urls
import cv_worker.operations.urls

from server import api


router = get_router()
router.register(r"settings", api.ServerSettingsViewSet, basename="BarryWilliams")

urlpatterns = [
  path('', include(router.urls)),
  path("api/v1/", include(router.urls)),
]
