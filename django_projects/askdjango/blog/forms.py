from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Comment
from .widgets import NaverMapPointWidget


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
        fields = ['title', 'content', 'point', 'photo']
        widgets = {
            'point': NaverMapPointWidget,
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', None)
        if title:
            if len(title) % 2 == 0:
                raise ValidationError('제목은 홀수로 입력하세요.')
            title = title.strip()  # 좌우 화이트 스페이스를 제거
        return title

    def clean(self):
        title = self.cleaned_data.get('title', '')
        content = self.cleaned_data.get('content', '')
        if len(title) + len(content) < 40:
            raise ValidationError('글자와 제목의 길이 합이 40자 이상 되도록 입력해주세요.')
        return self.cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

