from rest_framework import serializers
# Model
from QR.models.report import Report


class ReportSerializer(serializers.ModelSerializer):
    """Report Serializer"""
    week = serializers.DateField()
    class Meta:
        model = Report
        fields = '__all__'
