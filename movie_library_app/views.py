from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Movie
from .models import Review
from .models import Actor
from .models import BonusInfo
from .forms import MovieForm
from .forms import BonusInfoForm
from .forms import ReviewForm


@login_required
def test_response(request):
    return HttpResponse("<h1>First test</h1>")


def all_movies(request):
    movies = Movie.objects.all()
    return render(request, "movie.html", {"movies": movies})


@login_required()
def new_movie(request):
    movie_form = MovieForm(request.POST or None, request.FILES or None)
    bonus_form = BonusInfoForm(request.POST or None)

    if all((movie_form.is_valid(), bonus_form.is_valid())):
        movie = movie_form.save(commit=False)
        bonus = bonus_form.save()
        movie.bonus_info = bonus
        movie.save()
        return redirect(all_movies)

    return render(
        request,
        "movie_form.html",
        {"form": movie_form, "bonus_form": bonus_form, "new": True},
    )


@login_required()
def edit_movie(request, id):

    movie = get_object_or_404(Movie, pk=id)

    try:
        bonus = BonusInfo.objects.get(movie=movie.id)
    except ObjectDoesNotExist:
        bonus = None

    try:
        rev = Review.objects.filter(film=movie)
    except ObjectDoesNotExist:
        rev = None

    movie_form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    bonus_form = BonusInfoForm(request.POST or None, instance=bonus)
    review_form = ReviewForm(request.POST or None)

    if request.method == "POST":
        if "stars" in request.POST:
            review = review_form.save(commit=False)
            review.film = movie
            review.save()

    if all((movie_form.is_valid(), bonus_form.is_valid())):
        movie = movie_form.save(commit=False)
        bonus_info = bonus_form.save()
        movie.bonus_info = bonus_info
        movie.save()
        return redirect(all_movies)
    return render(
        request,
        "movie_form.html",
        {
            "form": movie_form,
            "bonus_form": bonus_form,
            'rev': rev,
            'review_form': review_form,
            "new": False,
        },
    )


def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == "POST":
        movie.delete()
        return redirect(all_movies)

    return render(request, "confirm.html", {"movie": movie})
