from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('api.urls.user_urls')),
    path('api/',include('api.urls.bot_urls')) # ->checked
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # for development only
# still both urlpatterns needs to understand
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) # for development only