from watchlist_app.models import WatchList,StreamPlatform,Reviews
from watchlist_app.api.serializers import (WatchListSerializer,StreamPlatformSerializer,
                                           ReviewsSerializer)
from watchlist_app.api.permissions import AdminOrReadOnly,ReviewUserOrReadOnly


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework import mixins
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


class WatchListAV(APIView):
    
    def get(self, request,):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
        
        
class WatchDetailsAV(APIView):
    
    def get(self, request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'not found'},status = status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def put(self, request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie,data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk):
        
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
        
        



# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_201_CREATED)
        

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




class ReviewList(generics.ListAPIView):
    # queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reviews.objects.filter(watchlist=pk)
    
class ReviewCreate(generics.CreateAPIView):
   
    serializer_class = ReviewsSerializer  
    def get_queryset(self):
        return Reviews.objects.all()
    
    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        print(review_user)
        review_queryset = Reviews.objects.filter(watchlist=watchlist,review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("already a review")
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2
            
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()
        serializer.save(watchlist = watchlist,review_user = review_user)
        
        
    

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    
    permission_classes = [ReviewUserOrReadOnly]



# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewDetails(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    

class StreamPlatformListAV(APIView):
    
    def get(self, request):
        Streamplatformlist = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(Streamplatformlist,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
class StreamPlatformDetailsAV(APIView):
    
    def get(self, request,pk):
        try:
            Streamplatformlist = StreamPlatform.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'not found'},status = status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(Streamplatformlist)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def put(self, request,pk):
        Streamplatformlist = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(Streamplatformlist,data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk):
        
        Streamplatformlist = StreamPlatform.objects.get(pk=pk)
        Streamplatformlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
