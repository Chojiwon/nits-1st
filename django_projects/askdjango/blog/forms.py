from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Comment


def min_length_10_validator(value):
    if len(value) < 10:
        raise ValidationError('10글자 이상 입력해주세요.')


class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_10_validator])
    content = forms.CharField()
    author = forms.CharField()

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

