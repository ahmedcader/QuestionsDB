from django.db import models
from category.models import Category
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(editable=True, null=False, blank=False)

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_post_user(self):
        return self.user

    def get_post_category(self):
        return self.category