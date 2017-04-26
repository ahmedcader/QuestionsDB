from django.conf.urls import url, include
from register.views import RegisterPage

urlpatterns = [
    url(r'^', RegisterPage.as_view(), name='register_page'),
]