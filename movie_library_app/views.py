from django.shortcuts import render, get_object_or_404
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

    return render(request, 'new_movie.html', {'form': form})


def edit_movie(request, id):
    form = get_object_or_404(Movie, pk=id)


def delete_movie(request):
    pass