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


class PetDetails(View):
    def get(self, request):
        return render(request, "core/details.html", locals())
