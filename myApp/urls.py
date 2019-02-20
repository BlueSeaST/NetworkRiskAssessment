from django.conf.urls import url

from . import views

urlpatterns = [
    url('login', views.login),
    url('index', views.index),
    url('MyProfile', views.profile),
    url('logout', views.logout),
    url('draw', views.draw),
]