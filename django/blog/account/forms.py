from django import forms

from account import models

class RegisterForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        max_length=32,
        min_length=6,
        widget=forms.TextInput()
    )

    password = forms.CharField(
        label="输入密码",
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput()
    )

    password2 = forms.CharField(
        label="确认密码",
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput()
    )
