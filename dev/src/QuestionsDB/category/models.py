from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    sub_category = models.ForeignKey('self', blank=True, null=True, related_name='subcategory')
    slug = models.SlugField(null=True, blank=True, auto_created=True, unique=False)

    def __str__(self):
        if self.sub_category is not None:
            return '{0} in {1}'.format(self.get_name(), self.sub_category.get_name())
        return self.name

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_slug(self):
        slug = slugify(self.get_name())
        return slug

    def get_id(self):
        return self.id

    def get_sub_name(self):
        return self.sub_category.get_name()

    def get_all_children(self):
        parents = []
        p = self.sub_category
        while p:
            parents.append(p)
            p = p.sub_category
        parents.reverse()
        return parents
