from django import forms
from django.core.exceptions import ValidationError


def min_length_10_validator(value):
    if len(value) < 10:
        raise ValidationError('10글자 이상 입력해주세요.')


class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_10_validator])
    content = forms.CharField()
    author = forms.CharField()

