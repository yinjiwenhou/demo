from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import UserModel, UserToken

class SimpleTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):

        token = request.META.get('HTTP_TOKEN', b'')

        try:
            user_token = UserToken.objects.get(token=token)
        except UserToken.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')

        user = user_token.user
        return (user, user_token)



