from django.conf.urls import patterns, url
from login import views

 
urlpatterns = patterns('',
    url(r'^$', views.login1, name='login1'),
    url(r'^$', views.login, name='login'),
)
