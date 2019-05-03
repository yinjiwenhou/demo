from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import RegisteSerialzier, LoginSerializer, ProfileSerializer
from.models import UserProfile, UserToken, UserModel


def generate_token(username):
    import time
    import hashlib
    token = hashlib.md5()
    token.update(username.encode("utf8"))
    token.update(time.ctime().encode("utf8"))
    return token.hexdigest()

class RegisteView(APIView):

    def post(self, request, *args, **kwargs):
        ser = RegisteSerialzier(data=request.data)
        if ser.is_valid():
            username = ser.data['username']
            password = ser.data['password']
            email = ser.data['email']
            phone = ser.data['phone']
            user = UserModel.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()

            userProfile = UserProfile(user=user, phone=phone)
            userProfile.save()

            token = generate_token(username)
            UserToken.objects.update_or_create(user=user, token=token)

            resp = {"token": token}
            return Response(resp, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        ser = LoginSerializer(data=request.data)
        if ser.is_valid():
            user = UserModel.objects.get(username=ser.data['username'])
            if user.check_password(ser.data['password']):
                token = user.usertoken.token
                resp = {"token": token}
                return Response(resp, status=status.HTTP_200_OK)
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
        else:
            Response(ser.error, status=status.HTTP_400_BAD_REQUEST)


from .authentications import SimpleTokenAuthentication
from .permissions import SelfReadPremisssion

class ProfileView(APIView):

    authentication_classes = [SimpleTokenAuthentication,]
    permission_classes = [SelfReadPremisssion,]

    def get(self, request, *args, **kwagrs):
        user_id = kwagrs.get("id", None)
        # user = UserModel.objects.get(username=request.user)
        user = UserModel.objects.get(pk=user_id)
        ser = ProfileSerializer(user.userprofile)
        ser.data["user"].pop("password")
        return Response(ser.data, status=status.HTTP_200_OK)

