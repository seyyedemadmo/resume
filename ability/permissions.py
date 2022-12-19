from rest_framework import permissions


class OnlyAdminCanCreate(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.user.is_authenticated and request.user.is_superuser) or view.action == 'list':
            return True
        return False
