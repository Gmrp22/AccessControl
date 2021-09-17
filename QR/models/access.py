from django.db import models
from .user import User
from datetime import date, time
import datetime as dt


class Access(models.Model):
    """Access Model"""
    STATE = (
        ('IN', 'IN'),
        ('OUT', 'OUT'),
    )

    def default_start_time():
        now = dt.time
        return now

    date = models.DateField(default=date.today)
    entry_time = models.TimeField(auto_now_add=True)
    departure_time = models.TimeField(auto_now=True)
    status = models.CharField(choices=STATE, null=True,
                              blank=True, max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_access')
