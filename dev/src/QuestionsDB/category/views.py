from django.shortcuts import render
from category.models import Category


def category_page(request, category_slug):
    parent = request.GET.get('p')
    child = request.GET.get('c')
    category = Category.objects.get(id=parent, sub_category_id=child)
    if parent is not None and child is not None:
        sub_categories = Category.objects.filter(sub_category_id=parent)
    else:
        sub_categories = Category.objects.filter(sub_category__name=category_slug)
    context = {'sub_categories': sub_categories, 'category': category, }
    return render(request, 'category.html', context)
    # return render(request, 'category.html')
