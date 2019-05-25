from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

from account import forms, models
from account.Token import token

def signup(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            user_token = token.get_token(username)

            send_mail(
                '注册成功',
                '',
                'xxx@163.com',
                [form.cleaned_data['email']],
                html_message='<h2>{user}</h2><hr><p>点击<a href="{url}">此处</a>激活</p>'.format(user=username,url=request.build_absolute_uri(reverse('active')) + '?token='+user_token),
                fail_silently=False,
            )

            return render(request, 'account/activation.html')
        else:
            print(form.errors)
    else:
        form = forms.RegisterForm()

    return render(request, 'account/signup.html', {'form': form})

def active(request):
    user_token = request.GET.get('token')
    try:
        username = token.confirm_token(user_token)
    except:
        return HttpResponse(u'对不起，验证链接已经过期')

    try:
        user = models.User.objects.get(username=username)
    except models.User.DoesNotExist:
        HttpResponse(u'对不起，您所验证的用户不存在，请重新注册')

    user.is_active = True
    user.save()
    return HttpResponse(u'激活成功')

