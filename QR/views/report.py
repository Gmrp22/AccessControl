from QR.serializers.user import UserSerializer
from QR.serializers.access import AccessSerializer
from os import access
from rest_framework import viewsets, status
from datetime import date
from rest_framework.response import Response
# Models
from QR.models.report import Report
from QR.models.user import User
from QR.models.qr import QR
from QR.models.access import Access
# Serializer
from QR.serializers.report import ReportSerializer

from django.db.models import Count, Sum, Avg


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()

    def get_serializer_class(self):
        """Define serializer"""
        return ReportSerializer
