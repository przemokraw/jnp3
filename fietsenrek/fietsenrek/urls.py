from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls,),
    url(r'^accounts/', include('allauth.urls', namespace='accounts')),
    url(r'^racks/', include('racks.urls', namespace='racks')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
