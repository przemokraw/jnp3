from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    url(r'^create/$', views.RackCreateView.as_view(), name='create'),
    url(r'^list/$', cache_page(60 * 3)(views.RackListView.as_view()), name='list'),
    url(r'^top/$', cache_page(60 * 5)(views.RackTopListView.as_view()), name='top'),
    url(r'^(?P<pk>\d+)/downvote/$', views.RackDownVoteView.as_view(), name='downvote'),
    url(r'^(?P<pk>\d+)/upvote/$', views.RackUpVoteView.as_view(), name='upvote'),
    url(r'^(?P<pk>\d+)/solve/$', views.RackSolveView.as_view(), name='solve'),
    url(r'^problems/$', views.RackProblems.as_view(), name='problems')
]
