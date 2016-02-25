'''
Created on Feb 23, 2016

@author: mehrab
'''

from django.conf.urls import url
# from django.contrib import admin
# from posts.views import post_home
# from . import views
from .views import (post_list, post_create, post_details, post_update, post_delete,)

urlpatterns = [
#     url(r'^posts/$', post_home),
#     url(r'^$', 'posts.views.post_home'),
#     url(r'^$', 'posts.views.post_list'),
#     url(r'^create/$', 'posts.views.post_create'),
#     url(r'^details/$', 'posts.views.post_details'),
#     url(r'^update/$', 'posts.views.post_update'),
#     url(r'^delete/$', 'posts.views.post_delete'),
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_details, name='details'),
    url(r'^(?P<id>\d+)/update/$', post_update, name='update'),
    url(r'^delete/$', post_delete),
]