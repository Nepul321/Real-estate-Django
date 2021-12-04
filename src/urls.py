from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from src.settings import MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('authentication.urls')),
    path('', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)