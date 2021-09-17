from rest_framework import serializers
# Model
from QR.models.user import User


class UserSerializer(serializers.ModelSerializer):
    """User Serializer"""
    # id = serializers.IntegerField(default=0)
    class Meta:
        model = User
        fields = '__all__'


class UserAccessSerializer(serializers.ModelSerializer):
    """User Serializer"""
    class Meta:
        model = User
        fields = ['carnet']
