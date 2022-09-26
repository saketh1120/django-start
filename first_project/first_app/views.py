from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Topic, Webpage, AccessRecord, UserInfo, UserProfileUpdate
from .forms import MyNewForm, FormName, UserUpdateForm, UserForm
from django import forms

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    context_dict = {"text": "you are using template filters here to title case this content"}
    return render(request, "first_app/index.html",context=context_dict)


def template(request):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records": webpages_list}

    # my_dict = {"insert_me":"Hello I am from first_app/views.py"}
    return render(request, "first_app/basic_templates.html", context=date_dict)


def help(request):
    my_dict = {"help_Page": "I needed help so i visited this page"}
    return render(request, "first_app/help.html", context=my_dict)


def userinfo(request):
    form = MyNewForm()

    if request.method == "POST":
        form = MyNewForm(request.POST)

        if form.is_valid():
            form.save()

            return index(request)

        else:
            forms.ValidationError("Please fill the fields correctly")
            print("Error: invalid Data")

    return render(request, "first_app/users.html", {"form": form})

    # user_list = Users.objects.order_by("first_name")
    # user_dict = {"user_list": user_list}
    # return render(request, "first_app/users.html", context=user_dict)


@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/first_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect("register")

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserUpdateForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "user_image" in request.FILES:
                profile.user_image = request.FILES["user_image"]

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserUpdateForm()

    return render(request, "first_app/registration.html", {"user_form": user_form,
                                                           "profile_form": profile_form,
                                                           "registered": registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("index")

            else:
                return HttpResponse("Account is not active")

        else:
            print("Someone tried to login and failed")
            print(f"username:{username}, password: {password}")
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, "first_app/login.html", {})


def form_view(request):
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)


        if form.is_valid():
            print("Your data is valid")
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Remarks: {form.cleaned_data['Remarks']}")
    return render(request, "first_app/basic_forms.html", {'form': form})

