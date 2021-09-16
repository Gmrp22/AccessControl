from rest_framework import viewsets, status
from rest_framework.response import Response
# Models
from QR.models.access import Access
# Serializer
from QR.serializers.access import AccessSerializer


class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()

    def get_serializer_class(self):
        """Define serializer"""
        return AccessSerializer

