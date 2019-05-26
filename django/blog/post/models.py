from django.db import models
from django.utils import timezone

from account.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (('draft', '草稿'), ('published', '已发布'))
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    published = PublishedManager()
    objects = models.Manager()
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)
