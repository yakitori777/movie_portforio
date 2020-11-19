from django.urls import path
from .views import movie_list_func,movie_detail_func, select_seat_func, login_error_func, readme_func, vue_movie_list_func
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', movie_list_func, name='movie_list'),
    path('detail/<int:pk>/', movie_detail_func, name='movie_detail'),
    path('seat/', select_seat_func, name='select_seat'),
    path('loginError/', login_error_func, name='login_error'),
    path('readme/', readme_func, name='readme'),
    path('movieList/', vue_movie_list_func, name='vue_movie_list'),
]
