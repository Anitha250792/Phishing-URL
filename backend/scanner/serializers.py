from rest_framework import serializers
from .models import Scan, ScanResult


class ScanResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanResult
        fields = "__all__"


class ScanSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()

    class Meta:
        model = Scan
        fields = "__all__"

    def get_result(self, obj):
        try:
            result = obj.result
            return ScanResultSerializer(result).data
        except:
            return None   # ✅ prevents 500 error when result not created yet
