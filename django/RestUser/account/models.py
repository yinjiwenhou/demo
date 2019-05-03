from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

class UserToken(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    token = models.CharField(max_length=32)
