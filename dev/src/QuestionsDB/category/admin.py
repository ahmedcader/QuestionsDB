from django.contrib import admin
from category.models import Category
from django import forms

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', "id", 'parent_id', 'description',]
    list_filter = ['name', 'parent', "id", 'parent_id', 'description',]
    search_fields = ['name', 'parent', "id", 'parent_id', 'description',]
    prepopulated_fields = {'slug': ('name',), }

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)
