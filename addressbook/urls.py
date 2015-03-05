from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import contacts.views

urlpatterns = patterns('',
                       url(r'^$', contacts.views.ListContactView.as_view(),
                           name='contacts-list',),
                       url(r'^tasks/', include('contacts.urls',
                                               namespace='contacts')),
                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout'),
                       )
urlpatterns += staticfiles_urlpatterns()
