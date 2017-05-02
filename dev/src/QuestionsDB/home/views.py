from django.shortcuts import render
from category.models import Category


def home_page(request):
    categories = Category.objects.filter(parent=None)
    context = {'categories': categories}
    return render(request, 'home.html', context)
