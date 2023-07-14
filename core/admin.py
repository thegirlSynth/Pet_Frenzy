from django.contrib import admin
from .models import Pet, PetUser, Cart, Payment, OrderPlaced, WishList, PetSold

# Register your models here.


@admin.register(Pet)
class PetModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "user", "price", "category", "pet_image"]


@admin.register(PetUser)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "locality", "city", "state", "zipcode"]


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "pet"]


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ["id", "ref", "amount", "verified", "date_created"]


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "petuser",
        "pet",
        "ordered_date",
        "status",
        "payment",
    ]


@admin.register(WishList)
class WishListModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "pet"]


@admin.register(PetSold)
class PetSoldModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "pet",
        "ordered_date",
        "status",
    ]
