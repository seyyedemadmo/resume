from rest_framework.permissions import BasePermission


class OnlyAdminOrListRetrieve(BasePermission):
    def has_permission(self, request, view):
        if (request.user.is_authenticated and request.user.is_superuser) or view.action == 'list' or view.action == 'retrieve':
            return True
        return False
