from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def login(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            form.save()
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("/")
    # else:
    #     return redirect("signup")
    form = SignUpForm()

    context = {
        "form": form
    }

    return render(request, "login.html", context)

def signup(request):
    # if request.user.is_anonymous: # i.e if user is logged out
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            form.save()
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("/")
    # else:
    #     return redirect("signup")
    form = SignUpForm()

    context = {
        "form": form
    }

    return render(request, "signup.html", context)