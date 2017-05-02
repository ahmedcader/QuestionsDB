from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from mptt.models import MPTTModel, TreeForeignKey

class Comment(MPTTModel):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    comment = models.TextField(editable=True, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now=True)
    date_edited = models.DateTimeField(auto_now=False)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['date_posted']

    def __str__(self):
        return "{0}".format(self.id)

    def get_comment(self):
        return self.comment

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
