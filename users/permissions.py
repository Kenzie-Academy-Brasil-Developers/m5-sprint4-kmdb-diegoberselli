import ipdb
from rest_framework import permissions


class UserIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method == "POST":
            return True
        return request.user.is_authenticated and request.user.is_superuser
