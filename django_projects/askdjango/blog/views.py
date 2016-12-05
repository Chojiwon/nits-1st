from django.http import Http404
from django.shortcuts import get_object_or_404, render
from blog.models import Post


def post_list(request):
    return render(request, 'blog/post_list.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })

