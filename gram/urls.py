from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^welcome/$',views.welcome,name='index'),
    url(r'^$', views.home, name = 'welcome'),
]