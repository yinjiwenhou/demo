from django.shortcuts import render

from post import models

def index(request):
    posts = models.Post.published.all()
    return render(request, 'post/index.html', {'posts': posts})
