from django.contrib import admin
from .models import Pet

# Register your models here.


@admin.register(Pet)
class PetModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category", "pet_image"]
