from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=512, unique=True)
    image = models.ImageField(upload_to='movie_images/')
    categories = ArrayField(models.CharField(max_length=128))
    description = models.TextField()
    pegi = models.PositiveSmallIntegerField()
    rating = models.FloatField()
    countries = ArrayField(models.CharField(max_length=128))
    duration = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
