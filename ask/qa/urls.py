from qa.views import test
from django.conf.urls import url, include
#from django.conf.urls.defaults import *

urlpatterns = [url(r'^$', test)]
