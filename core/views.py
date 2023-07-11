from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import Pet, PetUser, Cart, Payment, OrderPlaced, WishList
from .forms import UserRegistrationForm, UserProfileForm, UserPasswordResetForm
from django.contrib import messages
from django.conf import settings
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
def homepage_view(request):
    """
    Returns the homepage of the website.
    """
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))
    return render(request, "core/home.html", locals())


def aboutpage_view(request):
    """
    Returns the about page of the website.
    """
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))
    return render(request, "core/about.html", locals())


def contactpage_view(request):
    """
    Returns the about page of the website.
    """
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))
    return render(request, "core/contact.html", locals())


class CategoryView(View):
    """
    Returns the requested categories
    """

    def get(self, request, value):
        pets = Pet.objects.filter(category=value)
        names = Pet.objects.filter(category=value).values("name")
        breeds = pets.values_list("breed", flat=True).distinct()
        category = value

        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))

        return render(request, "core/category.html", locals())


class BreedView(View):
    def get(self, request, category, value):
        pets = Pet.objects.filter(breed=value)
        names = Pet.objects.filter(breed=value, category=category).values("name")
        breeds = Pet.objects.values_list("breed", flat=True).distinct()
        category = category

        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))

        return render(request, "core/breed.html", locals())


class CategoryName(View):
    def get(self, request, value):
        pets = Pet.objects.filter(name=value)
        names = Pet.objects.filter(category=pets[0].category).values("name")

        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))

        return render(request, "core/category.html", locals())


class PetDetails(View):
    def get(self, request, num):
        pet = Pet.objects.get(id=num)

        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            wishlist = WishList.objects.filter(Q(pet=pet) & Q(user=request.user))
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))

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


@method_decorator(login_required, name="dispatch")
class ProfileView(View):
    def get(self, request):
        form = UserProfileForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))
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


@login_required
def address_view(request):
    address = PetUser.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))
    return render(request, "core/address.html", locals())


@method_decorator(login_required, name="dispatch")
class UpdateAddress(View):
    def get(self, request, pk):
        add = PetUser.objects.get(pk=pk)
        form = UserProfileForm(instance=add)

        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))
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


@login_required
def addtocart_view(request):
    user = request.user
    pet_id = request.GET.get("pet_id").replace("/", "")
    pet = Pet.objects.get(id=pet_id)
    Cart(user=user, pet=pet).save()
    return redirect("/cart")


@login_required
def showcart_view(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for pt in cart:
        value = pt.quantity * pt.pet.price
        amount = amount + value
    totalamount = amount + 2500

    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))

    return render(request, "core/addtocart.html", locals())


@login_required
def wishlist(request):
    user = request.user
    pets = WishList.objects.filter(user=user)

    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))

    return render(request, "core/wishlist.html", locals())


@login_required
def pluscart_view(request):
    if request.method == "GET":
        pet_id = request.GET["pet_id"]
        cd = Cart.objects.get(Q(pet=pet_id) & Q(user=request.user))
        cd.quantity += 1
        cd.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.pet.price
            amount = amount + value
        totalamount = amount + 2500
        data = {"quantity": cd.quantity, "amount": amount, "totalamount": totalamount}
        return JsonResponse(data)


@login_required
def minuscart_view(request):
    if request.method == "GET":
        pet_id = request.GET["pet_id"]
        cd = Cart.objects.get(Q(pet=pet_id) & Q(user=request.user))
        cd.quantity -= 1
        cd.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.pet.price
            amount = amount + value
        totalamount = amount + 2500
        data = {"quantity": cd.quantity, "amount": amount, "totalamount": totalamount}
        return JsonResponse(data)


@login_required
def removecart_view(request):
    if request.method == "GET":
        pet_id = request.GET["pet_id"]
        cd = Cart.objects.get(Q(pet=pet_id) & Q(user=request.user))
        cd.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.pet.price
            amount = amount + value
        totalamount = amount + 2500
        data = {"amount": amount, "totalamount": totalamount}
        return JsonResponse(data)


@login_required
def orders(request):
    order_placed = OrderPlaced.objects.filter(user=request.user)

    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))

    return render(request, "core/orders.html", locals())


@method_decorator(login_required, name="dispatch")
class checkout_view(View):
    def get(self, request):
        user = request.user
        address = PetUser.objects.filter(user=user)
        uid = address
        cart_items = Cart.objects.filter(user=user)
        amount = 0
        for p in cart_items:
            value = p.quantity * p.pet.price
            amount = amount + value
        totalamount = amount + 2500

        email = user.email
        paystack_pub_key = settings.PAYSTACK_PUBLIC_KEY

        new_pay = Payment.objects.create(amount=totalamount, email=email, user=user)
        new_pay.save()

        payment = model_to_dict(new_pay)
        amount_value = new_pay.amount_value()

        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(WishList.objects.filter(user=request.user))

        return render(request, "core/checkout.html", locals())


@login_required
def verify_payment(request, ref, uid):
    payment = Payment.objects.get(ref=ref)
    verified = payment.verify_payment()

    if verified:
        payment.verified = True

        petuser = PetUser.objects.get(id=uid)
        cart = Cart.objects.filter(user=request.user)
        for c in cart:
            OrderPlaced(
                user=request.user,
                petuser=petuser,
                pet=c.pet,
                quantity=c.quantity,
                payment=payment,
            ).save()
            c.delete()

        return redirect("orders")


def plus_wishlist(request):
    if request.method == "GET":
        pet_id = request.GET["pet_id"]
        pet = Pet.objects.get(id=pet_id)
        user = request.user
        WishList(user=user, pet=pet).save()
        data = {
            "message": "Added to wishlist!",
        }
        return JsonResponse(data)


def minus_wishlist(request):
    if request.method == "GET":
        pet_id = request.GET["pet_id"]
        pet = Pet.objects.get(id=pet_id)
        user = request.user
        WishList.objects.filter(user=user, pet=pet).delete()
        data = {
            "message": "Removed from wishlist!",
        }
        return JsonResponse(data)


def search(request):
    query = request.GET["search"]
    pets = Pet.objects.filter(
        Q(breed__icontains=query)
        | Q(category__icontains=query)
        | Q(name__icontains=query)
    )

    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))

    return render(request, "core/search.html", locals())
