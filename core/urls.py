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
    ProfileView,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, PasswordResetForm


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
    path("profile/", ProfileView.as_view(), name="profile"),
    path("address/", ProfileView.as_view(), name="address"),
    #
    # login authentication
    #
    path(
        "accounts/login/",
        auth_view.LoginView.as_view(
            template_name="core/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    path("signup/", UserRegistrationView.as_view(), name="signup"),
    path(
        "password-reset/",
        auth_view.PasswordResetView.as_view(
            template_name="core/password-reset.html", form_class=PasswordResetForm
        ),
        name="password-reset",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
