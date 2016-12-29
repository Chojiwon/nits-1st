from django.conf import settings
from django.core.files import File
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from blog.utils import thumbnail


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d')
    point = models.CharField(max_length=100, blank=True,
            validators=[RegexValidator(r'^[+-]?[\d\.]+,[+-]?[\d\.]+$')])
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)  #'auth.User')
    author = models.CharField(max_length=20)
    tags = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return '/blog/{}'.format(self.pk)
        return reverse('blog:post_detail', args=[self.pk])

    def as_dict(self):
        if self.photo:
            photo_url = self.photo.url
        else:
            photo_url = None

        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'photo_url': photo_url,
            'point': self.point,
            'writer': self.writer.username,
            'author': self.author,
            'tag_set': self.tag_set.all(),
            'updated_at': self.updated_at,
        }


def on_pre_save_post(sender, **kwargs):
    post = kwargs['instance']
    if post.photo:
        max_width = 300
        if post.photo.width > max_width or post.photo.height > max_width:
            processed_f = thumbnail(post.photo.file, max_width, max_width)
            post.photo.save(post.photo.name, File(processed_f), save=False)

pre_save.connect(on_pre_save_post, sender=Post)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

