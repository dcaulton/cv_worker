from server.router import get_router

from cv_worker.scanners import api

router = get_router()

router.register(
    r"scanners", api.ScannerViewSet, basename="CheechMarin"
)
