from django.conf.urls import patterns, url
from volunteer import views

urlpatterns = patterns('',
    url(r'^social/', views.social),
    url(r'^education/',views.education),
    url(r'^contact/',views.contact),
  
)