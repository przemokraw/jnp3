from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from accounts.views import FacebookLogin

urlpatterns = [
    url(r'^admin/', admin.site.urls,),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^racks/', include('racks.urls', namespace='racks')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
