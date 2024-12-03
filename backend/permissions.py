from rest_framework.permissions import BasePermission


class IsOwnerReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):    # Имеет ли право пользователь на работу с конкретным объектом
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user == obj