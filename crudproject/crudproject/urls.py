from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='display'),
    path('insert/', createproduct, name='insert'),
    path('update/<int:id>', updateproduct, name='update'),
    path('delete/<int:id>', deleteproduct, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)