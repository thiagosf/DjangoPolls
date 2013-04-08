from django.conf.urls import patterns, url

from galleries import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^gallery/(?P<gallery_id>\d+)/$', views.detail, name='detail'),
)