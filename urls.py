from django.urls import path
from django.contrib import admin
from two import views
from django.conf import settings  # Use lowercase 'settings'
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view/' , views.my_view),
    path('member', views.members_list)
]

# This line tells Django how to serve static assets during local development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
