from server.router import get_router

from cv_worker.scanners import api

router = get_router()

router.register(
    r"v1/scanners", api.ScannerViewSet, basename="CheechMarin"
)
