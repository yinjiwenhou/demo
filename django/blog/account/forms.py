from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from account import models

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="用户名",
        max_length=32,
        min_length=6,
        error_messages = {
            'min_length': '用户名不能少于6个字符',
            'max_length': '用户名不能多余32个字符',
            'required': '用户名不能为空'
        },
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label="邮箱",
        widget = forms.EmailInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label="输入密码",
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label="确认密码",
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = models.User
        fields = ('username', 'email', 'password1', 'password2')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        return user

