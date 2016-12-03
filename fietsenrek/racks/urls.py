from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.RackCreateView.as_view(), name='create'),
    url(r'^list/$', views.RackListView.as_view(), name='list'),
    url(r'^top/$', views.RackTopListView.as_view(), name='top'),
    url(r'^vote/$', views.RackVoteView.as_view(), name='vote'),
]
