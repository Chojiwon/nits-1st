from django.conf.urls import url
from django.http import JsonResponse
from blog.models import Post


def post_list(request):
    qs = Post.objects.all()

    post_list = [
        {'id': post.id, 'title': post.title}
        for post in qs
    ]

    return JsonResponse(post_list, safe=False, json_dumps_params={
        'indent': 4,
        'ensure_ascii': False,
    })


urlpatterns = [
    url(r'^posts/$', post_list, name='post_list'),
]

