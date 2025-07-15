from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),  # This will make the homepage the default page
    path('rooms/', include('room.urls')),
    path('admin/', admin.site.urls),
]
