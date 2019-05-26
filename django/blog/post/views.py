from django.shortcuts import render
from django.core.paginator import Paginator

from post import models

def index(request):
    post_list = models.Post.published.all()
    paginator = Paginator(post_list, 2)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(request, 'post/index.html', {'posts': posts})
