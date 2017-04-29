from django.contrib import admin
from posts.models import Post
from django import forms

# class MyModelForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(PostAdmin, self).__init__(*args, **kwargs)
#         self.initial['some_field'] = some_encoding_method(self.instance.some_field)

class PostAdmin(admin.ModelAdmin):

    # form = MyModelForm

    list_display = ['title', "id", "user", 'category', 'slug_field']
    list_filter = ['title', "id", "user", 'category']
    search_fields = ['title', "id", "user", 'category']
    prepopulated_fields = {'slug_field': ('title',), }

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
