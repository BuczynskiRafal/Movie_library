from django.forms import ModelForm
from .models import *


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "description", "release_date", "imdb_rating"]


class BonusInfoForm(ModelForm):
    class Meta:
        model = BonusInfo
        fields = ['duration', 'film_genre']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['stars', 'review']
