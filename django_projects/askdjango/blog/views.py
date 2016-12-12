from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Post
from blog.forms import PostForm


def post_list(request):
    # print(request.GET)
    # print(request.GET['age'], request.GET.get('age'))
    # print(request.GET['name'], request.GET.get('name'))
    # print(request.GET.getlist('name'))
    # print(request.POST)
    # print(request.FILES)
    return render(request, 'blog/post_list.html', {
        'post_list': Post.objects.all(),
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
#           post = Post(
#               title=form.cleaned_data['title'],
#               content=form.cleaned_data['content'],
#               author=form.cleaned_data['author'])
#           post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {
        'form': form,
    })

