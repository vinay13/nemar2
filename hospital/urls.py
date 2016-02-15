from django.conf.urls import patterns, url
from hospital import views

urlpatterns = patterns('',
    url(r'^hospitals/', views.hospital),
    
)
