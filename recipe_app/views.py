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
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")


class RecipeDetail(DetailView):
    model = Recipe

class RecipeDelete(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Recipe
    success_url = "home"

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.owner:
            return self.request.user

class RecipeUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Recipe
    fields = ["name", "description", "price", "image"]

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.owner:
            return self.request.user

    def form_valid(self, form):
        if form.instance.owner == self.request.user:
            return super().form_valid(form)

class RecipeCreate(CreateView, LoginRequiredMixin):
    model = Recipe
    fields = ["name", "description", "price", "image"]

    def form_valid(self, form):
        if form.instance.owner == self.request.user:
            return super().form_valid(form)