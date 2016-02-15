"""medics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from rest_framework_nested import routers
from authentication.views import AccountViewSet,groupdetails
from authentication.views import LoginView
from authentication.views import LogoutView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
 #   url(r'^health/', include('health.urls')),
    url(r'^volunteer/',include('volunteer.urls')),
    url(r'^patient/',include('patient.urls')),
    url(r'^doctor/',include('doctor.urls')),
    url(r'^hospital/',include('hospital.urls')),
    url(r'^userprofile/',include('userprofile.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/groups/',groupdetails),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^grappelli/',include('grappelli.urls')),
]

admin.site.site_header="Nemar"
