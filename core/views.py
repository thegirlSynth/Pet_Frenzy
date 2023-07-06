from django.db.models import Count
from django.shortcuts import render
from django.views import View
from .models import Pet


# Create your views here.
def homepage_view(request):
    """
    This is a function-based view that returns the homepage of the website.
    """
    return render(request, "core/home.html")


class CategoryView(View):
    """
    Returns the requested categories
    """

    def get(self, request, value):
        pets = Pet.objects.filter(category=value)
        names = Pet.objects.filter(category=value).values("name")
        return render(request, "core/category.html", locals())


class CategoryName(View):
    def get(self, request, value):
        pets = Pet.objects.filter(name=value)
        names = Pet.objects.filter(category=pets[0].category).values("name")
        return render(request, "core/category.html", locals())


class PetDetails(View):
    def get(self, request, num):
        pet = Pet.objects.get(pk=num)
        return render(request, "core/details.html", locals())
