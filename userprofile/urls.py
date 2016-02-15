from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from userprofile import views


urlpatterns = patterns('',
    url(r'^users/$', views.userprofile),
    url(r'^users/(?P<pk>[0-9]+)/$', views.userprofile_detail),
    
)
