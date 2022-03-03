from unicodedata import name
from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import (WatchListAV, WatchDetailsAV, 
                                     StreamPlatformListAV, StreamPlatformDetailsAV,
                                     ReviewList,ReviewDetails,ReviewCreate,
                                     StreamPlatformVS)



router = DefaultRouter()
router.register('streamplatform', StreamPlatformVS,basename = 'streamplatform')

urlpatterns = [
  
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>/',WatchDetailsAV.as_view(),name='movie-details'),
     path('', include(router.urls)),
    # path('streamplatform/',StreamPlatformListAV.as_view(),name='streamplatform-list'),
    # path('streamplatform/<int:pk>',StreamPlatformDetailsAV.as_view(),name='streamplatform-details'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create'),
    path('<int:pk>/reviews/',ReviewList.as_view(),name='review-list'),

    path('review/<int:pk>/',ReviewDetails.as_view(),name='review-details'),
]