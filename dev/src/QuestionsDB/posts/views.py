from django.shortcuts import render
from category.models import Category
from posts.models import Post


def posts_page(request, category_slug):
    child_id = request.GET.get('c')
    parent_id = request.GET.get('p')
    # print(category_slug, parent_id, child_id)

    category = Category.objects.get(id=parent_id)
    posts = Post.objects.filter(category_id=parent_id)
    context = {'posts': posts, 'category': category, }
    return render(request, 'posts.html', context)
