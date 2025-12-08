from django.urls import path
from .views import create_scan, scan_history

urlpatterns = [
    path("api/scan/", create_scan),
    path("api/history/", scan_history),
]
