from datetime import date
from rest_framework import viewsets, status
from rest_framework.response import Response
import qrcode
# Models
from QR.models.user import User
from QR.models.qr import QR
from QR.models.access import Access
from QR.models.report import Report
# Serializer
from QR.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        """Define serializer"""
        return UserSerializer

    def create(self, request):
        """User creation"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            img = qrcode.make(new_user.carnet)
            f = open("QRTemp/output" + new_user.carnet + ".png", "wb")
            img.save(f)
            f.close()
            new_QR = QR(image="QRTemp/output" +
                        new_user.carnet + ".png", user=new_user)
            new_QR.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
