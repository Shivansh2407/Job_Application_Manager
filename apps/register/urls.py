from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout', views.logout),
    url('^admin.html$', views.admincheck),
    url('^admin/check/$', views.admincheck),
    url('^admin/check/logout.html$', views.logout),
    url('^register/$', views.register_stud),
    url('^register.html$', views.register_stud),
    url(r'^homepage.html$', views.home),
    url(r'^register/index.html$', views.logagain),
    url(r'^admin/check/register/index.html$', views.logagain),
    url(r'^admin/check/show_students.html$', views.show_students),


]