from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
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


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

