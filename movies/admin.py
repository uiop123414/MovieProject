from django.contrib import admin
from movies.models import Movie


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'categories', 'pegi')
    fields = ('name', 'image', 'categories', 'description', 'pegi', 'rating', 'countries', 'duration', 'year')
    ordering = ('name',)
