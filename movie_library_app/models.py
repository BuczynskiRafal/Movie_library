from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True, default='Matrix')
    description = models.TextField(blank=True, unique=False, default='Sample description')
    release_date = models.DateField(unique=False, default='2000-01-01')
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, default=5)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({str(self.description)})"

    def movie_summary(self):
        movie_summary = f"The premiere of the film {self.title} took place on {self.release_date}"
        return movie_summary
