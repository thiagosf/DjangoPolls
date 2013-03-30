from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Polls.views.home', name='home'),

    url(r'^polls/', include('polls2.urls', namespace='polls2')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #(r'^grappelli/', include('grappelli.urls')),
)

urlpatterns += staticfiles_urlpatterns()