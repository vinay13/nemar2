from django.conf.urls import patterns, url
from doctor import views

urlpatterns = patterns('',
    url(r'^doctors/', views.doctorinfo),
    
)

