from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("create-recipe/", views.RecipeCreateView.as_view(), name="create-recipe"),
    path("update-recipe/<int:pk>/", views.RecipeUpdateView.as_view(), name="update-recipe"),
    path("recipe/<int:pk>/", views.RecipeDetailView.as_view(), name="recipe-detail"),
    path("delete-recipe/<int:pk>/", views.RecipeDeleteView.as_view(), name="delete-recipe"),
    path("search/", views.search, name="search")
]