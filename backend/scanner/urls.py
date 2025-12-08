from django.urls import path
from .views import create_scan, scan_history

urlpatterns = [
    path("scan/", create_scan),        # ✅ POST
    path("history/", scan_history),    # ✅ GET
]
