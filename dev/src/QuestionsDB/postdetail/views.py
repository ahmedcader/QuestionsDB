from django.shortcuts import render
from posts.models import Post
from category.models import Category
from comment.models import Comment
from datetime import datetime


def post_detail_page(request, category_slug, question_id, post_slug):
    post = Post.objects.get(id=question_id)
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments,}
    return render(request, 'post_detail.html', context)
