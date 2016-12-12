from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sum/(?P<numbers>[\d\/]+)/$', views.mysum, name='mysum'),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello, name='hello'),
    url(r'^post/$', views.post_list, name='post_list'),
]

