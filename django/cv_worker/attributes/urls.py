from server.router import get_router

from cv_worker.attributes import api

router = get_router()

router.register(
    r"attributes", api.AttributeViewSet, basename="PaulRubens"
)
