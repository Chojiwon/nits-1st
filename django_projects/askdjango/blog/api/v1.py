import json
from django.conf.urls import url
from django.http import HttpResponse
from blog.models import Post


def post_list(request):
    qs = Post.objects.all()

    post_list = [
        {'id': post.id, 'title': post.title}
        for post in qs
    ]

    json_string = json.dumps(post_list, indent=4, ensure_ascii=False)
    return HttpResponse(json_string)


urlpatterns = [
    url(r'^posts/$', post_list, name='post_list'),
]

