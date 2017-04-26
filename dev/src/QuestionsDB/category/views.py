from django.shortcuts import render
from category.models import Category


def category_page(request, category_name):
    category = Category.objects.get(name=category_name)
    categories = Category.objects.all()
    sub_categories = Category.objects.filter(sub_category__name=category_name)
    print(sub_categories.first())
    context = {'category': category,'categories': categories, 'sub_categories': sub_categories, }
    return render(request, 'category.html', context)