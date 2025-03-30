from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Removed duplicate
]

# Add this to serve static files in development & Render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
