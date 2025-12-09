import random
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Scan
from .serializers import ScanSerializer


# ✅ CREATE SCAN API (POST)
class ScanCreateView(generics.CreateAPIView):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer

    def create(self, request, *args, **kwargs):
        url = request.data.get("url")

        if not url:
            return Response(
                {"error": "URL is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        verdict = random.choice(["Safe", "Suspicious", "Phishing"])
        risk_score = random.randint(10, 95)

        scan = Scan.objects.create(
            url=url,
            verdict=verdict,
            risk_score=risk_score,
            reason="Scanning in progress"
        )

        serializer = self.get_serializer(scan)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ✅ GET SINGLE SCAN RESULT (GET)
class ScanDetailView(generics.RetrieveAPIView):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer
    lookup_field = "id"


# ✅ SCAN HISTORY (GET)
@api_view(["GET"])
def scan_history(request):
    scans = Scan.objects.all().order_by("-created_at")
    serializer = ScanSerializer(scans, many=True)
    return Response(serializer.data)
