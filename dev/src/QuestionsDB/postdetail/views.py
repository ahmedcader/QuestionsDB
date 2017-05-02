from django.shortcuts import render
from posts.models import Post
from category.models import Category
from comment.models import Comment
from datetime import datetime
from django.core.urlresolvers import reverse
from home import views


def post_detail_page(request, parent_id, parent_category_slug, question_id):
    post = Post.objects.get(id=question_id)
    comments = Comment.objects.filter(post=post)
    categories = Category.objects.get(id=parent_id)
    context = {'post': post, 'comments': comments,}
    return render(request, 'post_detail.html', context)
