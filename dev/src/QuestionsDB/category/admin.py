from django.contrib import admin
from category.models import Category
from django import forms

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', "id", 'description']
    list_filter = ["name"]
    search_fields = ["name"]
    prepopulated_fields = {'slug': ('name',), }

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)
