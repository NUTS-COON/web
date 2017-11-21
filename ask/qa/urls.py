from views import test
from django.conf.urls import url, include

urlpatterns = ['views', url(r'^$', include(test))]
