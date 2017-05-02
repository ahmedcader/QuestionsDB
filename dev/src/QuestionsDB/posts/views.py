from django.shortcuts import render
from category.models import Category
from posts.models import Post


def posts_page(request, parent_id, parent_category_slug):
    posts = Post.objects.filter(parent_id=parent_id)
    category = Category.objects.get(id=parent_id)
    context = {'posts': posts, 'category': category, }
    return render(request, 'posts.html', context)