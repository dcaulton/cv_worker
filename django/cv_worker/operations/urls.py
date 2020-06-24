from server.router import get_router

from cv_worker.operations import api

router = get_router()

router.register(r"v1/operations", api.OperationViewSet, basename="GeorgeCarlin")
router.register(r"v1/look-for-work", api.OperationLookForWorkViewSet, basename="RandyMeisner")
