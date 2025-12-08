import uuid
from django.db import models

class Scan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    verdict = models.CharField(max_length=20, default="Pending")
    risk_score = models.IntegerField(default=0)
    reason = models.TextField(default="Scanning in progress")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
