from server.router import get_router

from cv_worker.tasks import api

router = get_router()

router.register(
    r"tasks", api.TaskViewSet, basename="MitchHedburg"
)
