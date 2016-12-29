from django.contrib import admin
from django.utils.html import format_html
from blog.models import Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'link', 'get_content_size', 'created_at', 'updated_at']
    list_display_links = ['title', 'created_at']
    # list_editable = ['title']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']
    actions = ['send_push']

    def link(self, post):
        return format_html('<a href="http://naver.com">라라랜드 실시간 보기</a>')

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


admin.site.register(Comment)


admin.site.register(Tag)

