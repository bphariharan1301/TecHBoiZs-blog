from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myblog.urls')),
    path('admin/', admin.site.urls),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
