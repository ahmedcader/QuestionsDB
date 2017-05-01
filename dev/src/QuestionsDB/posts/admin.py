from django.contrib import admin
from posts.models import Post
from django import forms

class PostAdmin(admin.ModelAdmin):

    list_display = ['title', "id", "user", 'category', 'slug_field']
    list_filter = ['title', "id", "user", 'category']
    search_fields = ['title', "id", "user", 'category']
    prepopulated_fields = {'slug_field': ('title',), }

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
