from rest_framework import permissions

from users.models import ADMIN, MODERATOR


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow authors of an object to edit it.
    Assumes the model instance has an `author` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAdmin(permissions.BasePermission):
    """Object-level permissions to only allow users
    with 'admin' role to edit the object."""
    def has_permission(self, request, view):
        return ((hasattr(request.user, "role")
                 and request.user.role == ADMIN)
                or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return ((hasattr(request.user, "role")
                 and request.user.role == ADMIN)
                or request.user.is_superuser)


class IsModer(permissions.BasePermission):
    """Object-level permissions to only allow users
    with 'moderator' role to edit the object."""
    def has_permission(self, request, view):
        return (hasattr(request.user, "role")
                and request.user.role == MODERATOR)

    def has_object_permission(self, request, view, obj):
        return (hasattr(request.user, "role")
                and request.user.role == MODERATOR)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Permissions to only allow users with 'admin' role
    to edit the object, otherwise read-only access."""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and (request.user.is_staff or request.user.role == ADMIN))
