from django.shortcuts import render
from category.models import Category


def category_page(request, category_slug):
    # parent = request.GET.get('p')
    # child = request.GET.get('c')
    # print(category_slug)
    # category = Category.objects.get(id=parent, sub_category_id=child)
    # sub_categories = Category.objects.filter(sub_category_id=parent)
    # context = {'category': category, 'sub_categories': sub_categories, }
    # return render(request, 'category.html', context)
    return render(request, 'category.html')
