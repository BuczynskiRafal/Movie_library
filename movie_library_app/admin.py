from django.contrib import admin

from .models import Movie
from .models import BonusInfo

admin.site.register(Movie)
admin.site.register(BonusInfo)


# @admin.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
#     fields = ["title", "release_date"]  #wyświetli te elementy modelu
#     # exclude = ["description"]           #wyklucza te elementy modelu
#     # list_display = ["title", "release_date"]    #utworzy tabelę z kolumnami jak w liście
#     # list_filter = ("title", "release_date") #w tupli przekazane po czym sortować
#     # search_fields = ("title", "release_date") #wyszukiwanie w posanych w tupli parametrach
