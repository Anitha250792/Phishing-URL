from .ml.predictor import predict_url
from .models import Scan, ScanResult

def process_scan_task(scan_id):
    scan = Scan.objects.get(id=scan_id)

    verdict, score, reason = predict_url(scan.url)

    ScanResult.objects.create(
        scan=scan,
        verdict=verdict,
        risk_score=score,
        reason=reason
    )

    scan.status = "done"
    scan.save()   # ✅ THIS was missing before
