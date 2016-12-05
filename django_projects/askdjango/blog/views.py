from django.http import Http404
from django.shortcuts import render
from blog.models import Post


def post_list(request):
    return render(request, 'blog/post_list.html')


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })

