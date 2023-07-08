from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
    ("Imo", "Imo"),
    ("Kaduna", "Kaduna"),
    ("Port Harcourt", "Port Harcourt"),
    ("Abia", "Abia"),
    ("Enugu", "Enugu"),
    ("Bauchi", "Bauchi"),
    ("Makurdi", "Makurdi"),
    ("Bayelsa", "Bayelsa"),
    ("Delta", "Delta"),
    ("Lagos", "Lagos"),
    ("Abuja", "Abuja"),
    ("Other", "Other"),
)

CATEGORY_CHOICES = (
    ("DG", "Dog"),
    ("CT", "Cat"),
    ("HM", "Hamster"),
    ("FR", "Ferret"),
    ("SQ", "Squirrel"),
    ("HH", "Hedgehog"),
    ("GP", "GuineaPig"),
    ("CH", "Chinchilla"),
    ("AL", "Alpaca"),
    ("LL", "Llama"),
    ("OT", "Other"),
)


class Pet(models.Model):
    """
    Default storage class for pets
    """

    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age_in_weeks = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    pet_image = models.ImageField(upload_to="pet")

    def __str__(self):
        return self.name


class PetUser(models.Model):
    """
    Default class for Users
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name


class Cart(models.Model):
    """
    Default class for User carts
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.pet.price
