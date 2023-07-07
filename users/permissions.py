from rest_framework import permissions
from .models import UserModel
from rest_framework.views import View


class IsAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_superuser
    

class UserAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return request.user == obj