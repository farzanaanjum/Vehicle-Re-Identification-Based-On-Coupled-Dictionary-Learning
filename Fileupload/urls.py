"""Fileupload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
import app2.views
import RTO.views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('app2/', include('app2.urls')),
    url('RTO/', include('RTO.urls')),
    url(r'^signup', app2.views.signup, name='signup'),
    url(r'^register', RTO.views.register, name='register'),
    url(r'^index', app2.views.index, name='index'),
    url(r'^home', RTO.views.home, name='home'),
    url(r'^addvehicles', RTO.views.addvehicles, name='addvehicles'),
    url(r'^upadateCrime', app2.views.upadateCrime, name='upadateCrime'),
    url(r'^viewcrime', RTO.views.viewcrime, name='viewcrime'),
    url(r'^email', app2.views.email, name='email'),
    url(r'^otp', app2.views.otp, name='otp'),
]
