from django.conf.urls import include, url
from . import views
from . import views_cbv

urlpatterns = [
    url(r'^$', views_cbv.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views_cbv.post_edit, name='post_edit'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
]

urlpatterns += [
    url(r'^api/v1/', include('blog.api.v1', namespace='v1')),
    # url(r'^api/v2/', include('blog.api.v2', namespace='v2')),
    # url(r'^api/v3/', include('blog.api.v3', namespace='v3')),
]

