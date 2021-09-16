from django.db import models
from user import User
class QR(models.Model):
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_qr')
   