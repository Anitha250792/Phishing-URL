from django.urls import path
from .views import ScanCreateView, ScanDetailView, HistoryListView

urlpatterns = [
    path("scan/", ScanCreateView.as_view()),
    path("scan/<uuid:id>/", ScanDetailView.as_view()),  # ✅ FIXED
    path("history/", HistoryListView.as_view()),        # ✅ FIXED
]
