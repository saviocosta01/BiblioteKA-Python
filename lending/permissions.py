from rest_framework import permissions
from users.models import UserModel
from rest_framework.views import View


class LoanHistory(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: UserModel) -> bool:
        return request.user.is_superuser
