from django.conf.urls import url

from account import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^active/$', views.active, name='active'),
    url(r'^login/$', views.auth_login, name='login'),
    url(r'^logout/$', views.auth_logout, name='logout'),
]