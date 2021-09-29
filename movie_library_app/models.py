from django.db import models


class BonusInfo(models.Model):
    FILM_GENRE = {
        (0, 'Other'),
        (1, 'Comedy'),
        (2, 'Horror'),
        (3, 'Drama'),
        (4, 'Action')
    }
    duration = models.PositiveSmallIntegerField(default=120)
    film_genre = models.PositiveSmallIntegerField(default=0, choices=FILM_GENRE)


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True, default='Matrix')
    description = models.TextField(blank=True, unique=False, default='Sample description')
    release_date = models.DateField(unique=False, default='2000-01-01')
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, default=5)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    bonus_info = models.OneToOneField(BonusInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({str(self.release_date)})"

    def movie_summary(self):
        movie_summary = f"The premiere of the film {self.title} took place on {self.release_date}"
        return movie_summary


class Reviev(models.Model):
    review = models.TextField(default='', blank=True)
    stars = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Actor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    films = models.ManyToManyField(Movie)
