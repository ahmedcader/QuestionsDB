from django.contrib import admin
from posts.models import Post
from comment.models import Comment
from django import forms

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', "user", "post",'comment']
    list_filter = ['id', "user", "post",]
    search_fields = ['id', "user", "post",]

    class Meta:
        model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', "id", "user", 'parent', 'slug_field']
    list_filter = ['title', "id", "user", 'parent']
    search_fields = ['title', "id", "user", 'parent']
    prepopulated_fields = {'slug_field': ('title',), }

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
