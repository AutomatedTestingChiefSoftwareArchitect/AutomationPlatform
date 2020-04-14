from rest_framework.throttling import SimpleRateThrottle


class UserThrottle(SimpleRateThrottle):
    """重写用户登录访问频率get_cache_key方法"""
    scope = "DjangoRESTFramework"  # 自定义拦截信息key

    def get_cache_key(self, request, view):
        # 使用user来控制访问频率

        return request.user
