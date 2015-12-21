from django.conf.urls import patterns, url

from health import views

urlpatterns = patterns('',
    url(r'^bpchart/', views.bloodpressurechart),
    url(r'^mbg/',views.meanbloodglucose),
    url(r'^region/',views.region),
)


