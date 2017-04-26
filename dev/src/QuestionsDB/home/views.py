from django.shortcuts import render
from category.models import Category


def home_page(request):
    categories = Category.objects.filter(sub_category=None)
    context = {'categories': categories}
    return render(request, 'home.html', context)
