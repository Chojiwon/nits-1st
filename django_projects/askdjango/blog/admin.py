from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_content_size', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']
    actions = ['send_push']

    def get_content_size(self, post):
        return '{} 글자'.format(len(post.content))

    def send_push(self, request, queryset):
        # queryset  # FIXME: queryset 으로 수행
        for post in queryset:
            post.author
        total = queryset.count()
        self.message_user(request, '{}명에게 푸쉬를 보냈습니다.'.format(total))
    send_push.short_description = '지정 포스팅의 작성자에게 푸쉬를 보냅니다.'


admin.site.register(Post, PostAdmin)

