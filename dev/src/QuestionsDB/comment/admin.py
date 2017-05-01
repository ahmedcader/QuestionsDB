from django.contrib import admin
from comment.models import Comment

class CommentAdmin(admin.ModelAdmin):

    list_display = ['id', "user", "post",'comment']
    list_filter = ['id', "user", "post",]
    search_fields = ['id', "user", "post",]
    # prepopulated_fields = {'slug_field': ('title',), }

    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)