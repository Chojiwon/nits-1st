from django.conf.urls import url
from blog.models import Post


def post_list(request):
    return Post.objects.all()


def recent_post_list(request):
    return Post.objects.all().order_by('-id')[:10]


urlpatterns = [
    url(r'^posts/$', post_list, name='post_list'),
    url(r'^posts/recent/$', recent_post_list, name='recent_post_list'),
]

