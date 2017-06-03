from django.conf.urls import url, include
from django.contrib import admin
from registration.forms import RegistrationFormUniqueEmail

from registration.backends.default.views import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$',RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile/', include('Profile.urls')),
    url(r'^topics/(?P<parent_id>\d+)/(?P<parent_category_slug>[\w-]+)/', include('category.urls')),
    url(r'^', include('home.urls')),
]
