from django.conf.urls import url
from django.contrib import admin

from .views import (UserView,GetUser,UpdateUser,DestroyUser,AddUser,UserLoginAPIView)

urlpatterns=[
url(r'^$',UserView.as_view(),name="UserView"),
url(r'^create$',AddUser.as_view(),name="UserView"),
url(r'^login$',UserLoginAPIView.as_view(),name="UserView"),
url(r'^(?P<userid>[\w-]+)/$',GetUser.as_view(),name="GetUser"),
url(r'^(?P<userid>[\w-]+)/update$',UpdateUser.as_view(),name="UpdateUser"),
url(r'^(?P<userid>[\w-]+)/delete/$',DestroyUser.as_view(),name="DestroyUser"),


]