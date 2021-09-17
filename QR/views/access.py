from rest_framework import viewsets, status
from rest_framework.response import Response
# Models
from QR.models.access import Access
from QR.models.user import User
# Serializer
from QR.serializers.access import AccessSerializer
from time import  time
import datetime as dt

class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()

    def get_serializer_class(self):
        """Define serializer"""
        return AccessSerializer


