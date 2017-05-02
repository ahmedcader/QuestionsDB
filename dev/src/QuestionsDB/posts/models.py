from django.db import models
from category.models import Category
from django.contrib.auth.models import User
from django.utils.text import slugify
import hashlib

class Post(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(editable=True, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug_field = models.SlugField(null=True, blank=True, auto_created=True, unique=False)

    def __str__(self):
        return "{0}: {1} in {2}".format(self.get_title(), self.category.get_name(), self.category.parent.get_name())

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_slug(self):
        slug = slugify(self.get_title())
        return slug

    def get_body(self):
        return self.body

    def get_post_user(self):
        return self.user

    def get_date_posted(self):
        return self.date_posted

    def get_date_modified(self):
        return self.date_modified

    def get_post_category(self):
        return self.category
