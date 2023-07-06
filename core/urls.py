from django.urls import path
from .views import homepage_view, CategoryView, CategoryName, PetDetails, BreedView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", homepage_view, name="home"),
    path("category/<slug:value>", CategoryView.as_view(), name="category"),
    path("category-name/<value>", CategoryName.as_view(), name="category-name"),
    path(
        "category-breed/<category>/<value>", BreedView.as_view(), name="category-breed"
    ),
    path("pet-details/<int:num>", PetDetails.as_view(), name="pet-details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
