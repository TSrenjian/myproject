"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from board import views
from django.conf.urls import  url
urlpatterns = [
    url(r'^login/$',views.login,name='login'),
    url(r'^index/$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),#板块+主题
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'), #为某个板块新增主题
    #\d+将匹配任意大小的整数，(?P<pk>\d+)则将匹配到的这个整数赋给名为pk的关键字参数中
    url(r'^boards/(?P<pk>\d+)/topics/(?P<pk1>\d+)$',views.board_topic_posts,name='board_tpoic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<pk1>\d+)/new$',views.new_post,name='new_post'),
    url(r'^admin/', admin.site.urls),
]
