from django.shortcuts import render
from posts.models import Post
from category.models import Category
from comment.models import Comment
from datetime import datetime
from django.core.urlresolvers import reverse
from home import views
from django.http.response import HttpResponseRedirect


def post_detail_page(request, parent_id, parent_category_slug, question_id):
    post = Post.objects.get(id=question_id)
    comments = Comment.objects.filter(post=post)
    categories = Category.objects.get(id=parent_id)
    context = {'post': post, 'comments': comments, }
    user_comment = request.POST.get('user-comment')
    if request.POST:
        comment_parent = request.POST.get('reply-id')
        comment_obj = Comment(
            user=request.user,
            post=post,
            comment=user_comment,
            date_posted=datetime.now(),
            date_edited=datetime.now(),
            parent=Comment.objects.filter(id=comment_parent).first())
        comment_obj.save()
        return HttpResponseRedirect(request.path)
    return render(request, 'post_detail.html', context)
