from django.db import models

# Create your models here.

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
