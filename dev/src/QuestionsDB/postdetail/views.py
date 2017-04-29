from django.shortcuts import render
from posts.models import Post
from category.models import Category


def post_detail_page(request, category_slug, question_id, post_slug):
    child_id = request.GET.get('c')
    parent_id = request.GET.get('p')
    # print(category_slug, parent_id, child_id, post_slug)
    post = Post.objects.get(id=question_id)
    category = Category.objects.get(id=parent_id)
    print(category.get_name())
    context = {'category': category, 'post': post, }
    return render(request, 'post_detail.html', context)
