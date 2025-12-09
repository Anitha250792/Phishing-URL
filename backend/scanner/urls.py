from django.urls import path
from .views import ScanCreateView, ScanDetailView, scan_history

urlpatterns = [
    path("scan/", ScanCreateView.as_view(), name="create-scan"),
    path("scan/<uuid:id>/", ScanDetailView.as_view(), name="scan-detail"),
    path("history/", scan_history, name="scan-history"),
]
