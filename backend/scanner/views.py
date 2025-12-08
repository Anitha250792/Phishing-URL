from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Scan
from .serializers import ScanSerializer
import random

# ✅ CREATE SCAN (WORKING, NO CELERY)
@api_view(["POST"])
def create_scan(request):
    url = request.data.get("url")

    verdict = random.choice(["Safe", "Suspicious", "Phishing"])
    risk_score = random.randint(10, 95)

    scan = Scan.objects.create(
        url=url,
        verdict=verdict,
        risk_score=risk_score
    )

    serializer = ScanSerializer(scan)
    return Response(serializer.data)

# ✅ SCAN HISTORY
@api_view(["GET"])
def scan_history(request):
    scans = Scan.objects.all().order_by("-created_at")
    serializer = ScanSerializer(scans, many=True)
    return Response(serializer.data)
