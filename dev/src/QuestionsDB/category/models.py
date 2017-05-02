from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    slug = models.SlugField(null=True, blank=True, auto_created=True, unique=False)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
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
        return self.parent.get_name()

    # def get_all_children(self):
    #     parents = []
    #     p = self.sub_category
    #     while p:
    #         parents.append(p)
    #         p = p.sub_category
    #     parents.reverse()
    #     return parents
