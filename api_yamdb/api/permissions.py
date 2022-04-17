from rest_framework import permissions

from users.models import USER, MODERATOR, ADMIN


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow authors of an object to edit it.
    Assumes the model instance has an `author` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if ((hasattr(request.user, 'role') and request.user.role == ADMIN)
                or request.user.is_superuser):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if ((hasattr(request.user, 'role') and request.user.role == ADMIN)
                or request.user.is_superuser):
            return True
        return False


class IsModer(permissions.BasePermission):

    def has_permission(self, request, view):
        if hasattr(request.user, 'role') and request.user.role == MODERATOR:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, 'role') and request.user.role == MODERATOR:
            return True
        return False
