
from django.contrib import admin
from django.urls import path
from myapp.views import data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', data),
]
