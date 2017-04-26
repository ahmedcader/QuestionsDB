from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<category_id>\d+)/', views.posts_page, name='posts_page'),
]