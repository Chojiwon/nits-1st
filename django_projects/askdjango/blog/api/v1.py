from django.conf.urls import url
from django.http import JsonResponse
from blog.models import Post
from askdjango.encoders import CustomDjangoJSONEncoder


def post_list(request):
    qs = Post.objects.all()
    return JsonResponse(qs, encoder=CustomDjangoJSONEncoder, safe=False, json_dumps_params={
        'indent': 4,
        'ensure_ascii': False,
    })


urlpatterns = [
    url(r'^posts/$', post_list, name='post_list'),
]

