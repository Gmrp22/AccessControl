from rest_framework import serializers
# Model
from QR.models.report import Report


class ReportSerializer(serializers.ModelSerializer):
    """Report Serializer"""
    class Meta:
        model = Report
        fields = '__all__'
