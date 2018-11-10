from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index.*$', index, name='index'),
    url(r'^blog', blog, name='blog'),
    url(r'^gallery', gallery, name='gallery'),
    url(r'^contact', contact, name='contact'),

]