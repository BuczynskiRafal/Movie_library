from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def test_response():
    return HttpResponse("<h1>First test</h1>")


def all_movies(request):
    movies = Movie.objects.all()
    return render(request, "movie.html", {'message': movies})
