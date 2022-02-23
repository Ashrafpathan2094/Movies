from unicodedata import name
from django.urls import path,include
# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import MovieDetailsAV, MovieListAV

urlpatterns = [
  
    path('list/',MovieListAV.as_view(),name='movie-list'),
    path('<int:pk>',MovieDetailsAV.as_view(),name='movie-details'),
]