from QR.models.access import Access
from rest_framework import serializers
# Model
from QR.models.access import Access


class AccessSerializer(serializers.ModelSerializer):
    """Access Serializer"""
    class Meta:
        model = Access
        fields = '__all__'
        depth = 1
