from rest_framework import viewsets, status
from rest_framework.response import Response
# Models
from QR.models.report import Report
# Serializer
from QR.serializers.report import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()

    def get_serializer_class(self):
        """Define serializer"""
        return ReportSerializer

