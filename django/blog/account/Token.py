from django.conf import settings
from itsdangerous import URLSafeTimedSerializer
import base64

class Token():
    def __init__(self):
        self.secret_key = settings.SECRET_KEY
        # self.salt = base64.encodestring(self.secret_key)

    def get_token(self, username):
        serializer = URLSafeTimedSerializer(self.secret_key)
        return serializer.dumps(username)

    def confirm_token(self, token, expiration=3600):
        serializer = URLSafeTimedSerializer(self.secret_key)
        return serializer.loads(token, max_age=expiration)

token = Token()
