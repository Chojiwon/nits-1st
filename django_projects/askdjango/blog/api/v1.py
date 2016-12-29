import json
from django.conf.urls import url
from django.http import HttpResponse


def post_list(request):
    json_string = json.dumps([1, 2, 3, 4], indent=4)
    return HttpResponse(json_string)


urlpatterns = [
    url(r'^posts/$', post_list, name='post_list'),
]

