from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from .models import Scan, ScanResult
from .serializers import ScanSerializer, ScanResultSerializer
from .tasks import process_scan_task


# ✅ CREATE SCAN (SYNC VERSION - NO CELERY)
class ScanCreateView(CreateAPIView):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer

    def perform_create(self, serializer):
        scan = serializer.save(status="processing")

        # ✅ DIRECT FUNCTION CALL (instead of .delay())
        process_scan_task(str(scan.id))


# ✅ GET SCAN DETAILS
class ScanDetailView(generics.RetrieveAPIView):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer
    lookup_field = "id"   # ✅ REQUIRED for UUID lookup


# ✅ GET FINAL RESULT
class ScanResultView(RetrieveAPIView):
    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer

    def get(self, request, *args, **kwargs):
        scan_id = kwargs.get("id")

        try:
            result = ScanResult.objects.get(scan_id=scan_id)
            serializer = ScanResultSerializer(result)
            return Response(serializer.data)
        except ScanResult.DoesNotExist:
            return Response({"error": "Result not ready"}, status=404)


# ✅ HISTORY

class HistoryListView(generics.ListAPIView):
    queryset = Scan.objects.all().order_by("-created_at")
    serializer_class = ScanSerializer