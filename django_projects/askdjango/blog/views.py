from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Post, Comment
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

            messages.success(request, '새 포스팅을 저장했습니다.')

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

            messages.success(request, '포스팅을 수정했습니다.')

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

            messages.success(request, '새 댓글을 저장했습니다.')

            return redirect(comment.post) #  ... not iterable
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form': form,
    })


def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()

            messages.success(request, '댓글을 수정했습니다.')

            return redirect(comment.post)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {
        'form': form,
    })
