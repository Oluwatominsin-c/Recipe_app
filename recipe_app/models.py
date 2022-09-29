from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="recipes/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"pk":self.pk})