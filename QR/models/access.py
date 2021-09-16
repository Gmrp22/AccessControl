from django.db import models
from user import User
from datetime import date


class Access(models.Model):
    """Access Model"""
    STATE = (
        (IN, 'IN'),
        (OUT, 'OUT'),
    )
    date = models.DateField(default=date.today)
    entry_time = models.TimeField()
    departure_time = models.TimeField()
    status = models.CharField(choices=STATE, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_access')


      

