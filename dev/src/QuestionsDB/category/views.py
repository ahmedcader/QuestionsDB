from django.shortcuts import render
from category.models import Category


def category_page(request, parent_id, parent_category_slug):
    category = Category.objects.get(id=parent_id)
    categories = Category.objects.filter(parent_id=parent_id)
    print(categories)
    context = {'categories': categories, 'category': category, }
    # category = Category.objects.get(id=parent, sub_category_id=child)
    # sub_categories = Category.objects.filter(sub_category_id=parent)
    # context = {'category': category, 'sub_categories': sub_categories, }
    # return render(request, 'category.html', context)
    return render(request, 'category.html', context)
