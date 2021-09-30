from django.forms import ModelForm
from .models import *


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "description", "release_date", "imdb_rating"]

class BonusInfo(ModelForm):
    class Meta:
        model = BonusInfo
        fields = ['duration', 'film_genre']