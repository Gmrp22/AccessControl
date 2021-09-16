from rest_framework import viewsets, status
from rest_framework.response import Response
# Models
from QR.models.qr import QR
# Serializer
from QR.serializers.qr import QRSerializer


class QRViewSet(viewsets.ModelViewSet):
    queryset = QR.objects.all()

    def get_serializer_class(self):
        """Define serializer"""
        return QRSerializer

