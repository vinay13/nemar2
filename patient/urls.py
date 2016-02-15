from django.conf.urls import patterns, url
from patient import views


urlpatterns = patterns('',
    url(r'^social/',views.socialinfo),
    url(r'^health/',views.healthinfo),
    url(r'^financial/',views.financialinfo),
)


