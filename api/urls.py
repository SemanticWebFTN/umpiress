from django.conf.urls import patterns, url

from api import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
