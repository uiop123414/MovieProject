from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from movies.models import Movie


# Create your views here.


class IndexView(ListView):
    model = Movie
    template_name = 'movies/index.html'
    title = 'FlixGo – Online Movies, TV Shows & Cinema HTML Template'

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = self.title

        return context


class MovieView(TemplateView):
    model = Movie
    template_name = 'movies/movie.html'

    def get_context_data(self, **kwargs):
        context = super(MovieView, self).get_context_data()
        context['movie'] = Movie.objects.filter(id=kwargs.get('id')).first()
        return context
