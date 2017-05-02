from django.shortcuts import render
from category.models import Category
from posts.models import Post


def category_page(request, parent_id, parent_category_slug):
    category = Category.objects.get(id=parent_id)
    categories = Category.objects.filter(parent_id=parent_id)
    context = {'categories': categories, 'category': category, }
    return render(request, 'category.html', context)
