from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register', include('register.urls')),
    url(r'^login', include('login.urls')),
    url(r'^logout', include('logout.urls')),
    url(r'^profile/', include('Profile.urls')),
    url(r'^topics/(?P<parent_id>\d+)/', include('category.urls')),
    url(r'^', include('home.urls')),
]
