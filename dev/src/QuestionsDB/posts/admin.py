from django.contrib import admin
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', "user", "category", 'title', 'body',]
    list_filter = ['id', "user", "category", 'title', 'body',]
    search_fields = ['id', "user", "category", 'title', 'body',]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
