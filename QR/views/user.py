from rest_framework import viewsets, status
from rest_framework.response import Response
# Models
from QR.models.user import User
# Serializer
from QR.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        """Define serializer"""
        return UserSerializer

