from django.contrib import admin
from .models import Pet, PetUser, Cart, Payment, OrderPlaced

# Register your models here.


@admin.register(Pet)
class PetModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category", "pet_image"]


@admin.register(PetUser)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "locality", "city", "state", "zipcode"]


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "pet", "quantity"]


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
        "quantity",
        "ordered_date",
        "status",
        "payment",
    ]
