from django.db import models
from PIL import Image


# Create your models here.

class Recipe(models.Model):
    id = models.IntegerField(default=0, primary_key=True, unique=True)
    ingredient = models.TextField(default="salt")
    recipe = models.TextField(default="None")
    picture = models.ImageField(default='default.jpg', upload_to='photos', blank=True)

    def __str__(self):
        return self.recipe
