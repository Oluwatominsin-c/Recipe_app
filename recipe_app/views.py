from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Recipe


# Create your views here.

def home(request):
    user = request.user
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes,
        "user": user
    }
    return render(request, "recipe_app/index.html", context)

def about(request):
    return render(request, "recipe_app/about.html")


def search(request):
    return render(request, "recipe_app/search.html")

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Recipe
    success_url = "/"

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.owner
             

class RecipeUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Recipe
    fields = ["name", "description", "price", "image"]

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.owner
            

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class RecipeCreateView(CreateView, LoginRequiredMixin):
    model = Recipe
    # success_url = "/" 
    fields = ["name", "description", "price", "image"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)