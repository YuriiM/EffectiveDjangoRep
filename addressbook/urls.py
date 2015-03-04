# TODO: contacts urls move to contacts app
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import contacts.views

urlpatterns = patterns('',
                       url(r'^$', contacts.views.ListContactView.as_view(),
                           name='contacts-list',),
                       url(r'^new$', contacts.views.CreateContactView.as_view(),
                           name='contacts-new',),
                       url(r'^edit/(?P<pk>\d+)/$',
                           contacts.views.UpdateContactView.as_view(),
                           name='contacts-edit',),
                       url(r'^delete/(?P<pk>\d+)/$',
                           contacts.views.DeleteContactView.as_view(),
                           name='contacts-delete',),
                       url(r'^(?P<pk>\d+)/$', contacts.views.ContactView.as_view(),
                           name='contacts-view',),
                       )
urlpatterns += staticfiles_urlpatterns()
