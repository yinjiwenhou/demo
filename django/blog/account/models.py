from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        (1, '男'),
        (2, '女'),
    )
    nickname = models.CharField(blank=True, null=True, max_length=20)
    avatar = models.ImageField(upload_to='avatar')
    mobile = models.CharField(blank=True, null=True, max_length=13)
    gender = models.IntegerField(choices=GENDER_CHOICES,blank=True, null=True)


