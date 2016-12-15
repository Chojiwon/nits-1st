from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Post
from blog.forms import PostForm, PostModelForm, CommentForm


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
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # ModelForm way
            post.author = request.META['REMOTE_ADDR']
            post.save()

            # return redirect('blog:post_detail', post.id)
            # return redirect(post.get_absolute_url())
            return redirect(post)
    else:
        form = PostModelForm()

    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()  # ModelForm way
            # return redirect('blog:post_detail', post.id)
            # return redirect(post.get_absolute_url())
            return redirect(post)
    else:
        form = PostModelForm(instance=post)

    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(comment.post) #  ... not iterable
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form': form,
    })

