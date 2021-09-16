from rest_framework import serializers
# Model
from models.user import User


class UserSerializer(serializers.ModelSerializer):
    """User Serializer"""
    class Meta:
        model = User
        fields = '__all__'
