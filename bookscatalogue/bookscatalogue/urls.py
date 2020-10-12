#bookscatalogue URL Configuration

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/v1/', include('customerapi.urls')),
    path('books/v1/', include('bookapi.urls')),
]
