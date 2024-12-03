from rest_framework import serializers
from .models import Product, Shop, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser']
        read_only_fields = ['email',]