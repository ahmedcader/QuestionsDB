from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<category_name>[\w\-]+)/', views.posts_page, name='posts_page'),
]