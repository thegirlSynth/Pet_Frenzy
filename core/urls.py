from django.urls import path
from .views import (
    homepage_view,
    aboutpage_view,
    contactpage_view,
    CategoryView,
    CategoryName,
    PetDetails,
    BreedView,
    UserRegistrationView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", homepage_view, name="home"),
    path("about/", aboutpage_view, name="about"),
    path("contact/", contactpage_view, name="contact"),
    path("category/<slug:value>", CategoryView.as_view(), name="category"),
    path("category-name/<value>", CategoryName.as_view(), name="category-name"),
    path(
        "category-breed/<category>/<value>", BreedView.as_view(), name="category-breed"
    ),
    path("pet-details/<int:num>", PetDetails.as_view(), name="pet-details"),
    # login authentication
    path("login/", UserRegistrationView.as_view(), name="login"),
    path("signup/", UserRegistrationView.as_view(), name="signup"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
