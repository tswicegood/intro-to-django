from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.PeopleListView.as_view(), name="people_list"),
    url(r'^(?P<pk>[0-9]+)/$', views.PersonView.as_view(), name="person"),
)
