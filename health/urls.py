from django.conf.urls import patterns, url

from health import views

urlpatterns = patterns('',
    url(r'^bpchart/', views.bloodpressurechart),
    url(r'^mbg/',views.meanbloodglucose),
 #   url(r'^region/',views.region),
    url(r'^doctors/',views.doctorList),
    url(r'^medop/',views.medicaloperate),
    url(r'^socialinfo/',views.socialinfo),
    url(r'^healthinfo/',views.healthinfo),
    url(r'^financialinfo/',views.financialinfo),

)


