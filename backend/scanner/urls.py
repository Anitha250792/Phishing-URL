from django.urls import path
from .views import create_scan, scan_result, scan_history

urlpatterns = [
    path("scan/", create_scan),
    path("scan/<uuid:scan_id>/", scan_result),
    path("history/", scan_history),
]
