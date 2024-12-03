
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from backend.models import User
from backend.permissions import IsOwnerReadOnly
from backend.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def destroy(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj != request.user:
    #         raise PermissionDenied("Вы не можете удалить другого пользователя.")
    #     return super().destroy(request, *args, **kwargs)


def validate_quantity(value):
    if value < 0:
        raise ValidationError('Количество не может быть отрицательным.')








