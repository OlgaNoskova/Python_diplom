
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from backend.models import User
from backend.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def validate_quantity(value):
    if value < 0:
        raise ValidationError('Количество не может быть отрицательным.')








