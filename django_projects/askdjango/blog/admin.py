from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_content_size', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']

    def get_content_size(self, post):
        return '{} 글자'.format(len(post.content))


admin.site.register(Post, PostAdmin)

