from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Scan
from .serializers import ScanSerializer
import random

# ✅ CREATE SCAN API (POST /api/scan/)
class ScanCreateView(CreateAPIView):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer

    def perform_create(self, serializer):
        url = self.request.data.get("url")

        verdict = random.choice(["Safe", "Suspicious", "Phishing"])
        risk_score = random.randint(10, 95)

        serializer.save(
            url=url,
            verdict=verdict,
            risk_score=risk_score,
            reason="Scanning in progress"
        )

# ✅ SCAN HISTORY API (GET /api/history/)
@api_view(["GET"])
def scan_history(request):
    scans = Scan.objects.all().order_by("-created_at")
    serializer = ScanSerializer(scans, many=True)
    return Response(serializer.data)
