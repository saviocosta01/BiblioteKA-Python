from rest_framework import permissions
from .models import UserModel
from rest_framework.views import View


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: UserModel) -> bool:
        if request.method in permissions.SAFE_METHODS and request.user.is_superuser:
            return True
  

