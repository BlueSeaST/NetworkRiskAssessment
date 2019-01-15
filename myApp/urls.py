from django.conf.urls import url

from . import views

urlpatterns = [
    url('login', views.login),
    url('authenticate', views.authenticate),
    url('index', views.index),




    url('tables', views.tables),
    url('draw', views.draw),

]