
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    url(r'^login',views.login,name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^home',views.home,name='home'),
    url(r'^addvehicles', views.addvehicles, name='addvehicles'),

]

urlpatterns += staticfiles_urlpatterns()
