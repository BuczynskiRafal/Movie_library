from django.contrib import admin
from django.urls import path
from movie_library_app.views import *

urlpatterns = [
    path('test/', test_response),
    path('movies/', all_movies),
    path('new/', new_movie),
    path('edit/<int: id>/', edit_movie),
    path('delete/<int: id>', delete_movie)
]
