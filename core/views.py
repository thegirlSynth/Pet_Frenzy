from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from .models import Pet, PetUser, Cart
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib import messages


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


class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "core/userregistration.html", locals())

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! Welcome aboard.")
        else:
            messages.warning(request, "Invalid input data")
        return render(request, "core/userregistration.html", locals())


class ProfileView(View):
    def get(self, request):
        form = UserProfileForm()
        return render(request, "core/profile.html", locals())

    def post(self, request):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data["name"]
            locality = form.cleaned_data["locality"]
            city = form.cleaned_data["city"]
            mobile = form.cleaned_data["mobile"]
            zipcode = form.cleaned_data["zipcode"]
            state = form.cleaned_data["state"]

            newUser = PetUser(
                user=user,
                name=name,
                locality=locality,
                city=city,
                mobile=mobile,
                zipcode=zipcode,
                state=state,
            )
            newUser.save()
            messages.success(request, "Congratulations! Profile updated.")
        else:
            messages.warning(request, "Invalid input data")

        return render(request, "core/profile.html", locals())


def address_view(request):
    address = PetUser.objects.filter(user=request.user)
    return render(request, "core/address.html", locals())


class UpdateAddress(View):
    def get(self, request, pk):
        add = PetUser.objects.get(pk=pk)
        form = UserProfileForm(instance=add)
        return render(request, "core/updateaddress.html", locals())

    def post(self, request, pk):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            add = PetUser.objects.get(pk=pk)
            add.user = request.user
            add.name = form.cleaned_data["name"]
            add.locality = form.cleaned_data["locality"]
            add.city = form.cleaned_data["city"]
            add.mobile = form.cleaned_data["mobile"]
            add.zipcode = form.cleaned_data["zipcode"]
            add.state = form.cleaned_data["state"]
            add.save()
            messages.success(request, "Congratulations! Profile updated.")
        else:
            messages.warning(request, "Invalid input data")

        return redirect("address")


def addtocart_view(request):
    user = request.user
    pet_id = request.GET.get("pet_id").replace("/", "")
    pet = Pet.objects.get(id=pet_id)
    Cart(user=user, pet=pet).save()
    return redirect("/cart")


def showcart_view(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for pt in cart:
        value = pt.quantity * pt.pet.price
        amount = amount + value
    totalamount = amount + 40
    return render(request, "core/addtocart.html", locals())
