from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = 'Must be the owner of this post.'
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user
