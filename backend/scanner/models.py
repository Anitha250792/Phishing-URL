# scanner/models.py
import uuid
from django.db import models

class Scan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    normalized_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, default="queued")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url


class ScanResult(models.Model):
    scan = models.OneToOneField(Scan, on_delete=models.CASCADE, related_name="result")
    verdict = models.CharField(max_length=50)
    risk_score = models.FloatField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.verdict
