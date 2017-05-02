from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<parent_id>\d+)/(?P<parent_category_slug>[\w-]+)/$', views.posts_page, name='posts_page'),
    url(r'^(?P<parent_id>\d+)/(?P<parent_category_slug>[\w-]+)/', include('postdetail.urls')),
]