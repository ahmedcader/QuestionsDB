from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^', LoginPage.as_view(), name='login_page'),
    url(r'^', views.login_page, name='login_page'),
]