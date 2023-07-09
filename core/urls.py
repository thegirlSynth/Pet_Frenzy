from django.urls import path
from .views import (
    homepage_view,
    aboutpage_view,
    contactpage_view,
    address_view,
    CategoryView,
    CategoryName,
    PetDetails,
    BreedView,
    UserRegistrationView,
    ProfileView,
    UpdateAddress,
    addtocart_view,
    showcart_view,
    pluscart_view,
    minuscart_view,
    removecart_view,
    checkout_view,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import (
    LoginForm,
    UserPasswordResetForm,
    PasswordChangeForm,
    UserSetPasswordForm,
)


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
    path("address/", address_view, name="address"),
    path("update-address/<int:pk>", UpdateAddress.as_view(), name="update-address"),
    path("add-to-cart/", addtocart_view, name="add-to-cart"),
    path("cart/", showcart_view, name="show-cart"),
    path("checkout", checkout_view.as_view(), name="checkout"),
    path("pluscart", pluscart_view),
    path("minuscart", minuscart_view),
    path("removecart", removecart_view),
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
        "password-change/",
        auth_view.PasswordChangeView.as_view(
            template_name="core/change-password.html",
            form_class=PasswordChangeForm,
            success_url="/passwordchangedone",
        ),
        name="password-change",
    ),
    path(
        "passwordchangedone/",
        auth_view.PasswordChangeDoneView.as_view(
            template_name="core/passwordchangedone.html"
        ),
        name="passwordchangedone",
    ),
    path("logout/", auth_view.LogoutView.as_view(next_page="login"), name="logout"),
    #
    # Password Reset
    #
    path(
        "password_reset/",
        auth_view.PasswordResetView.as_view(
            template_name="core/password-reset.html",
            form_class=UserPasswordResetForm,
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_view.PasswordResetDoneView.as_view(
            template_name="core/passwordresetdone.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(
            template_name="core/passwordresetconfirm.html",
            form_class=UserSetPasswordForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete/",
        auth_view.PasswordResetCompleteView.as_view(
            template_name="core/passwordresetcomplete.html"
        ),
        name="password_reset_complete",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
