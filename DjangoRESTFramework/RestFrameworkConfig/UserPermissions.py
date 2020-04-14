from rest_framework.permissions import BasePermission


class AdminPermissions(BasePermission):
    """重写权限认证has_permission方法"""
    message = "User is not Admin"  # 用户权限拦截msg

    def has_permission(self, request, view):
        if request.user.user_type == 6:
            return True  # True有权限访问
        return False

