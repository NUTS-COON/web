from qa.views import test
from django.conf.urls import url
from qa.views import test, questions_list, popular, question, ask

urlpatterns = [
    url(r'^$', questions_list, name='questions_list'),
    url(r'^login/', test, name='test'),
    url(r'^signup/', test, name='test'),
    url(r'^question/(?P<num>[0-9]+)/$', question, name='question'),
    url(r'^ask/', ask, name='ask'),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', test, name='test')
]
