from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminorReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


# "token": "1d6127d53d4c61518f0d8ae6f426705802a68991"
