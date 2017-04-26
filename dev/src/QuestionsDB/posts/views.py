from django.shortcuts import render
from category.models import Category


def posts_page(request, category_name):
    print(category_name)
    return render(request, 'posts.html')
