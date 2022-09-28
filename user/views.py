from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm, UserCreationForm


def login(request):
    return render(request, "login.html")

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        pass
    else:
        form = SignUpForm()

    context = {
        "form": form
    }

    return render(request, "signup.html", context)