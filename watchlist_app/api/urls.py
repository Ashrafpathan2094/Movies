from unicodedata import name
from django.urls import path,include
# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import (WatchListAV, WatchDetailsAV, 
                                     StreamPlatformListAV, StreamPlatformDetailsAV,
                                     ReviewList,ReviewDetails,ReviewCreate)

urlpatterns = [
  
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',WatchDetailsAV.as_view(),name='movie-details'),
    path('streamplatform/',StreamPlatformListAV.as_view(),name='streamplatform-list'),
    path('streamplatform/<int:pk>',StreamPlatformDetailsAV.as_view(),name='streamplatform-details'),
 
    path('streamplatform/<int:pk>/review',ReviewList.as_view(),name='review-list'),
    path('streamplatform/<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),
    path('streamplatform/review/<int:pk>',ReviewDetails.as_view(),name='review-details'),
]