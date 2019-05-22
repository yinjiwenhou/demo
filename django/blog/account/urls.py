from django.conf.urls import url

from account import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
]