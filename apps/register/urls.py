from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout', views.logout),
    url('^admin$', views.adminpage),
    url('^admin/check/$', views.admincheck),
    url('^admin/check/logout.html$', views.logout),
    url('^apply.html$', views.apply),
    url(r'^homepage.html$', views.home),
    url(r'^register/index.html$', views.logagain),
    url(r'^admin/check/register/index.html$', views.logagain),

]