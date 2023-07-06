from django.db.models import Count
from django.shortcuts import render
from django.views import View
from .models import Pet


# Create your views here.
def homepage_view(request):
    """
    Returns the homepage of the website.
    """
    return render(request, "core/home.html")


def aboutpage_view(request):
    """
    Returns the about page of the website.
    """
    return render(request, "core/about.html")


def contactpage_view(request):
    """
    Returns the about page of the website.
    """
    return render(request, "core/contact.html")


class CategoryView(View):
    """
    Returns the requested categories
    """

    def get(self, request, value):
        pets = Pet.objects.filter(category=value)
        names = Pet.objects.filter(category=value).values("name")
        breeds = pets.values_list("breed", flat=True).distinct()
        category = value
        return render(request, "core/category.html", locals())


class BreedView(View):
    def get(self, request, category, value):
        pets = Pet.objects.filter(breed=value)
        names = Pet.objects.filter(breed=value, category=category).values("name")
        breeds = Pet.objects.values_list("breed", flat=True).distinct()
        category = category
        return render(request, "core/breed.html", locals())


class CategoryName(View):
    def get(self, request, value):
        pets = Pet.objects.filter(name=value)
        names = Pet.objects.filter(category=pets[0].category).values("name")
        return render(request, "core/category.html", locals())


class PetDetails(View):
    def get(self, request, num):
        pet = Pet.objects.get(pk=num)
        return render(request, "core/details.html", locals())
