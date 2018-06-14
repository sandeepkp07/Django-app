from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'signup/', views.SignUp.as_view(), name='signup'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
    url(r'show/$', views.show, name='show'),
    url(r'add/$', views.add, name='add'),
    url(r'twitter/$', views.tweets, name='tweets'),
    url(r'converter/$', views.converter, name='converter'),
    url(r'rssreader/$', views.rssreader, name='rssreader'),
    url(r'chatroom/$', views.chatroom, name='chatroom'),
]

