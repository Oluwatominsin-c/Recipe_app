from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes
    }
    return render(request, "index.html", context)