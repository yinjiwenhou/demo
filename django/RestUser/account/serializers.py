from rest_framework import serializers
from .models import UserModel, UserProfile

class RegisteSerialzier(serializers.Serializer):
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=32)
    email = serializers.EmailField()
    phone = serializers.IntegerField()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=32)

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = "__all__"
        depth=1
