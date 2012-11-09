from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),

    url(r'^add/goal', views.add_goal, name='add_goal'),

    url(r'^add/action', views.add_action, name='add_action'),
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
