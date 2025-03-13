from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('common.urls')),
    path('carweb/',include('carweb.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)