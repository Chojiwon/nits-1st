from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import Post, Comment
from blog.forms import PostForm, PostModelForm, CommentForm

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post, form_class=PostModelForm)

post_edit = UpdateView.as_view(model=Post, form_class=PostModelForm)

