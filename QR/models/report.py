from datetime import datetime,date
from django.db import models
from .user import User
from .access import Access

class Report(models.Model):
    """Report Model"""
    worked = models.FloatField()
    extra = models.FloatField()
    count = models.IntegerField(default=0)
    status = models.CharField(default="Open", max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_report')


