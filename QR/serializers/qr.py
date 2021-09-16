from rest_framework import serializers
# Model
from QR.models.qr import QR


class QRSerializer(serializers.ModelSerializer):
    """QR Serializer"""
    class Meta:
        model = QR
        fields = '__all__'
