from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor


# Create your views here.
def show_all_movies(request):
    movies = Movie.objects.all()
    rez = {"movies": movies}
    return render(request, 'movie_app/all_movies.html', context=rez)


def show_one_movie(request, slug_movie: str):
    # movie = Movie.objects.get(id=id_movie)
    movie = get_object_or_404(Movie, slug=slug_movie)
    rez = {"movie": movie}
    return render(request, 'movie_app/one_movie.html', context=rez)


def show_all_directors(request):
    directors = Director.objects.all()
    context = {'directors': directors}
    return render(request, 'movie_app/all_directors.html', context=context)


def show_one_director(request, id_direct: int):
    director = Director.objects.get(id=id_direct)
    # director = get_object_or_404(Director, slug=slug_direct)
    context = {"director": director}
    return render(request, 'movie_app/one_director.html', context=context)


def show_all_actors(request):
    actors = Actor.objects.all()
    context = {'actors': actors}
    return render(request, 'movie_app/all_actors.html', context=context)


def show_one_actor(request, id_actor: int):
    actor = Actor.objects.get(id=id_actor)
    # director = get_object_or_404(Director, slug=slug_direct)
    context = {"actor": actor}
    return render(request, 'movie_app/one_actor.html', context=context)

