from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.category_page, name='category_page'),
    url(r'^(?P<parent_id>\d+)/(?P<parent_category_slug>[\w-]+)/$', views.category_page, name='category_page'),
    url(r'^(?P<parent_id>\d+)/(?P<parent_category_slug>[\w-]+)/', include('posts.urls')),
]
