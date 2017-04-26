from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.logout_page, name='logout_page'),
]