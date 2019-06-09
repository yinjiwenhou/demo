from celery import Celery
from django.core.mail import send_mail
from django.conf import settings


import os

app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/0')

@app.task
def send_active_mail(to, username, token):
    subject = "欢迎注册"
    message = ""
    sender = settings.EMAIL_FROM
    receiver = [to]
    html_message = '<h1>{}, 欢迎注册</h1>点击链接激活<a href="http://127.0.0.1:8000/user/active/{}">激活</a>'.format(username, token)

    send_mail(subject, message, sender, receiver, html_message=html_message)
