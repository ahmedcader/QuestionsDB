from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<user_id>\d+)/(?P<user_name>[\w.@+-]+)$', views.profile_page, name='profile_page'),
]