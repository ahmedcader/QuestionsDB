from django.contrib import admin
from posts.models import Post
from django import forms

class PostAdmin(admin.ModelAdmin):

    list_display = ['title', "id", "user", 'parent', 'slug_field']
    list_filter = ['title', "id", "user", 'parent']
    search_fields = ['title', "id", "user", 'parent']
    prepopulated_fields = {'slug_field': ('title',), }

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
