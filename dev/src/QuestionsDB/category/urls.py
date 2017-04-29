from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.category_page, name='category_page'),
    url(r'^(?P<category_slug>[\w-]+)/$', views.category_page, name='category_page'),
    url(r'^(?P<category_slug>[\w-]+)/', include('posts.urls')),
]
