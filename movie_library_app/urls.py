from django.contrib import admin
from django.urls import path
from movie_library_app.views import *

urlpatterns = [
    path('test/', test_response),
    path('movies/', all_movies)
]
