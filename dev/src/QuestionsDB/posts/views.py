from django.shortcuts import render
from category.models import Category


def posts_page(request, category_id):

    print(Category.objects.get(id=category_id))
    return render(request, 'posts.html')
