from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    sub_category = models.ForeignKey('self', blank=True, null=True, related_name='subcategory')

    def __str__(self):
        return self.name

    def get_id(self):
        return self.id

    def get_sub_id(self):
        return self.sub_category.get_id()

    def get_description(self):
        return self.description

    def get_all_children(self, include_self=True):
        r = []
        if include_self:
            r.append(self)
        for c in Category.objects.filter(sub_category=self):
            _r = c.get_all_children(include_self=True)
            if 0 < len(_r):
                r.extend(_r)
        return r