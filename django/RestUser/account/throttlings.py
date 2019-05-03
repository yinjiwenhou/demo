from rest_framework.throttling import SimpleRateThrottle

class UserThrottle(SimpleRateThrottle):
    scope = "USER"
    def get_cache_key(self, request, view):
        return request.user.username


class IpThrottle(SimpleRateThrottle):
    scope = "IP"
    def get_cache_key(self, request, view):
        return request.META.get('REMOTE_ADDR')