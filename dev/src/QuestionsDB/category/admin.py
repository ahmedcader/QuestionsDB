from django.contrib import admin
from category.models import Category
from django import forms

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', "name", "sub_category", 'description']
    list_filter = ["name"]
    search_fields = ["name"]
    ordering = ('sub_category',)

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)
