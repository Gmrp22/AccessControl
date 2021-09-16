from django.db import models
from .user import User
from .access import Access

class Report(models.Model):
    """Report Model"""
    worked = models.FloatField()
    extra = models.FloatField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_report')
