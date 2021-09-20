from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def test_response(request):
    return HttpResponse("<h1>First test</h1>")


def all_movies(request):
    movies = Movie.objects.all()
    return render(request, "movie.html", {'message': [movies]})


def new_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, 'movie_form.html', {'form': form})


def edit_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)

    if form.is_valid():
        form.save()
        return redirect(all_movies)
    return render(request, 'movie_form.html', {'form': form})


def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == "POST":
        movie.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'movie': movie})
