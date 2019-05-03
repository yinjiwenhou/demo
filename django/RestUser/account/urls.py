from django.conf.urls import url

from account import views

urlpatterns = [
    url(r'^registe/$', views.RegisteView.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^profile/(?P<id>\d+)/$', views.ProfileView.as_view()),
]