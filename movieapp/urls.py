from django.urls import path
from .views import movie_detail_func, select_seat_func, login_error_func, readme_func, movie_list_func, vue_movie_list_func, vue_genre_movie_list_func
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('movieList/', movie_list_func, name='movie_list'),
    path('detail/<int:pk>/', movie_detail_func, name='movie_detail'),
    path('seat/', select_seat_func, name='select_seat'),
    path('loginError/', login_error_func, name='login_error'),
    path('readme/', readme_func, name='readme'),
    path('vueMovieList/', vue_movie_list_func, name='vue_movie_list'),
    path('vueGenreMovieList/', vue_genre_movie_list_func, name='vue_genre_movie_list'),
]
