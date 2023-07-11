from django.urls import path
from . import views as myviews
from django.contrib import admin
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
    path("", myviews.homepage_view, name="home"),
    path("about/", myviews.aboutpage_view, name="about"),
    path("contact/", myviews.contactpage_view, name="contact"),
    path("category/<slug:value>", myviews.CategoryView.as_view(), name="category"),
    path("pets/", myviews.CategoryName.as_view(), name="pets"),
    path("search", myviews.search, name="search"),
    path(
        "category-breed/<category>/<value>",
        myviews.BreedView.as_view(),
        name="category-breed",
    ),
    path("pet-details/<int:num>", myviews.PetDetails.as_view(), name="pet-details"),
    path("profile/", myviews.ProfileView.as_view(), name="profile"),
    path("address/", myviews.address_view, name="address"),
    path(
        "update-address/<int:pk>",
        myviews.UpdateAddress.as_view(),
        name="update-address",
    ),
    path("add-to-cart/", myviews.addtocart_view, name="add-to-cart"),
    path("cart/", myviews.showcart_view, name="show-cart"),
    path("wishlist/", myviews.wishlist, name="wishlist"),
    path("checkout", myviews.checkout_view.as_view(), name="checkout"),
    path("pluscart", myviews.pluscart_view),
    path("minuscart", myviews.minuscart_view),
    path("removecart", myviews.removecart_view),
    path("initiate_payment", myviews.checkout_view.as_view(), name="initiate_payment"),
    path(
        "verify-payment/<str:ref>/<int:uid>/",
        myviews.verify_payment,
        name="verify_payment",
    ),
    path("orders", myviews.orders, name="orders"),
    path("pluswishlist", myviews.plus_wishlist),
    path("minuswishlist", myviews.minus_wishlist),
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
    path("signup/", myviews.UserRegistrationView.as_view(), name="signup"),
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

admin.site.site_header = "Pet Frenzy"
admin.site.site_title = "Pet Frenzy"
admin.site.site_index_title = "Welcome to Pet Frenzy"
