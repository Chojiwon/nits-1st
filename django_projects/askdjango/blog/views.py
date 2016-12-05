from django.shortcuts import render
from blog.models import Post


def post_list(request):
    return render(request, 'blog/post_list.html')


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })

