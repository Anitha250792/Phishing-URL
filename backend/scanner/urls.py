from django.urls import path
from .views import ScanCreateView, scan_history

urlpatterns = [
    # ✅ Create Scan (POST)
    path("scan/", ScanCreateView.as_view(), name="scan-create"),

    # ✅ Scan History (GET)
    path("history/", scan_history, name="scan-history"),
]
