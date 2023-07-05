from django.urls import path
from .views import homepage_view, CategoryView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", homepage_view),
    path("category/<slug:value>", CategoryView.as_view(), name="category"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
