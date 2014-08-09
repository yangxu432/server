from django.conf.urls import *
urlpatterns = patterns('',
   url(r'^$','fvcom.views.index', name='index'),
)
