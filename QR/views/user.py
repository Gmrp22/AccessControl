
from django.core.mail.message import EmailMultiAlternatives
from rest_framework import viewsets, status
from rest_framework.response import Response
import qrcode
from AccessControl.settings import EMAIL_HOST_USER
# Models
from QR.models.user import User
from QR.models.qr import QR
# Serializer
from QR.serializers.user import UserSerializer
from email.mime.image import MIMEImage
from pathlib import Path


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
            img = qrcode.make(new_user.id)
            id= str(new_user.id)
            f = open("QRTemp/output" + id + ".png", "wb")
            img.save(f)
            f.close()
            
            new_QR = QR(image="QRTemp/output" +
                        id + ".png", user=new_user)
            new_QR.save()
            emailsend(new_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def emailsend(self):
    """Sets email info"""
    subject = 'QR CODE'
    message = "Codigo de acceso para  " + self.name + "  Carnet" + self.carnet
    recepient = self.email
    sender = EMAIL_HOST_USER
    id= str(self.id)
    image_path = "QRTemp/output" + id + ".png"
    image_name = Path(image_path).name
    html_message = f"""
    <!doctype html>
        <html lang=en>
            <head>
                <meta charset=utf-8>
                <title>Confirmacion de QR</title>
            </head>
            <body>
                <h1>{subject}</h1>
                <p>
                Imagen para acceso. {message}<br>
                <img src='cid:{image_name}'/>
                </p>
            </body>
        </html>
    """
    send_email(subject, message,  sender, recepient,
               html_message, image_path=image_path, image_name=image_name)


def send_email(subject, text_content,  sender, recipient, html_content=None, image_path=None,
               image_name=None):
    """Sends email"""
    email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sender,
                                   to=recipient if isinstance(recipient, list) else [recipient])

    if all([html_content, image_path, image_name]):
        email.attach_alternative(html_content, "text/html")
        email.content_subtype = 'html'
        email.mixed_subtype = 'related'
        with open(image_path, mode='rb') as f:
            image = MIMEImage(f.read())
            email.attach(image)
            image.add_header('Content-ID', f"<{image_name}>")
    email.send()
