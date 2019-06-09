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

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        max_length=32,
        widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '请输入用户名'}   
        )
    )

    password = forms.CharField(
        min_length=4,
        max_length=32,
        widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': '请输入密码'}
        )
    )


class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(
        label="昵称",
        min_length=3,
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )


    mobile = forms.CharField(
        label="手机",
        min_length=11,
        max_length=11,
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

    gender = forms.ChoiceField(
        label="性别",
        choices=((1, '男'), (2, '女')),
        required=False,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = models.User
        fields = ('nickname', 'mobile', 'gender')


class AvatarForm(forms.ModelForm):
    avatar = forms.FileField(
        label="头像",
        widget=forms.FileInput()
    )

    class Meta:
        model = models.User
        fields = ('avatar',)
