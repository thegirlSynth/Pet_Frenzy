from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import secrets
from .paystack import Paystack

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

STATUS_CHOICES = (
    ("Accepted", "Accepted"),
    ("Packed", "Packed"),
    ("On the way", "On the way"),
    ("Delivered", "Delivered"),
    ("Cancelled", "Cancelled"),
    ("Pending", "Pending"),
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


class Payment(models.Model):
    """
    Default class for Payments
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.FloatField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self):
        return f"Payment: {self.amount}"

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref

        super().save(*args, **kwargs)

    def amount_value(self):
        return int(self.amount) * 100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result["amount"] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False


class OrderPlaced(models.Model):
    """
    Default class for Placed Orders
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    petuser = models.ForeignKey(PetUser, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    @property
    def total_cost(self):
        return self.quantity * self.pet.price


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
