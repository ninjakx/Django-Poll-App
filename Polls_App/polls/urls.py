from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.Detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.Results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

