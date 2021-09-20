from django.contrib import admin
from django.urls import path
from movie_library_app.views import *

urlpatterns = [
    path('test/', test_response, name='test_response'),
    path('movies/', all_movies, name='all_movies'),
    path('new/', new_movie, name='new_movie'),
    path('edit/<int:id>/', edit_movie, name='edit_movie'),
    path('delete/<int:id>', delete_movie, name='delete_movie')
]
