from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Scan
from .serializers import ScanSerializer
import random


# ✅ CREATE SCAN
@api_view(["POST"])
def create_scan(request):
    url = request.data.get("url")

    verdict = random.choice(["Safe", "Suspicious", "Phishing"])
    risk_score = random.randint(10, 95)

    scan = Scan.objects.create(
        url=url,
        verdict=verdict,
        risk_score=risk_score,
        reason="AI risk analysis completed"
    )

    serializer = ScanSerializer(scan)
    return Response(serializer.data)


# ✅ GET SCAN RESULT
@api_view(["GET"])
def scan_result(request, scan_id):
    try:
        scan = Scan.objects.get(id=scan_id)
        serializer = ScanSerializer(scan)
        return Response(serializer.data)
    except Scan.DoesNotExist:
        return Response({"error": "Scan not found"}, status=404)


# ✅ HISTORY
@api_view(["GET"])
def scan_history(request):
    scans = Scan.objects.all().order_by("-created_at")
    serializer = ScanSerializer(scans, many=True)
    return Response(serializer.data)
