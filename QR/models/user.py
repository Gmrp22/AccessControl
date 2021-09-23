from django.db import models


class User(models.Model):
    """User Model"""
    name = models.CharField(max_length=100, null=False)
    carnet = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100, default="")