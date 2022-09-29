from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from .forms import SignUpForm, UserCreationForm



def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome {username}, you have succesfully registered!")
            return redirect("/login/")
    else:
        form = SignUpForm()

    context = {
        "form": form,
    }

    return render(request, "user/signup.html", context)


def profile(request):
    user = request.user
    context = {
        "user": user
    }
    return render(request, "user/profile.html", context)































# def signup(request):
#     # if request.user.is_anonymous: # i.e if user is logged out
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             form.save()
#             new_user = authenticate(username=username, password=password)
#             if new_user is not None:
#                 login(request, new_user)
#                 return redirect("/")
#     # else:
#     #     return redirect("signup")
#     form = SignUpForm()

#     context = {
#         "form": form
#     }

#     return render(request, "signup.html", context)