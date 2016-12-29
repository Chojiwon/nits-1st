from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comment_form': comment_form,
    })


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # ModelForm way
            post.author = request.META['REMOTE_ADDR']
            # 로그인 상황에서는 정상처리
            # 로그아웃 상황에서는 오류상황, request.user 는 AnonymousUser 인스턴스이기 때문
            post.writer = request.user
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


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=post)
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


def comment_list(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment_list = post.comment_set.all()
    return render(request, 'blog/comment_list.html', {
        'comment_list': comment_list,
    })


@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            if request.is_ajax():
                return {'ok': True, 'flash_message': '댓글이 잘 저장되었습니다.'}
            else:
                messages.success(request, '새 댓글을 저장했습니다.')
                return redirect(comment.post) #  ... not iterable
        else:
            return {'ok': False, 'errors': form.errors}
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form': form,
    })


@login_required
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

