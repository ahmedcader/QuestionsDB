from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^(?P<question_id>\d+)/(?P<url_slug>[\w-]+)', views.post_detail_page, name='post_detail_page'),
    url(r'^(?P<question_id>\d+)', views.post_detail_page, name='post_detail_page'),
]