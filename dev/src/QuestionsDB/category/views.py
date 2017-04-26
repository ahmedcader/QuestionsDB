from django.shortcuts import render
from category.models import Category


def category_page(request, category_id):
    category = Category.objects.get(id=category_id)
    categories = Category.objects.all()
    sub_categories = Category.objects.filter(sub_category_id=category_id)
    context = {'category': category,'categories': categories, 'sub_categories': sub_categories, }
    return render(request, 'category.html', context)