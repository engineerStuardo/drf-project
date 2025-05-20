from rest_framework import status, generics

from watchlist_app.models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer


class WatchListView(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


class WatchListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


class StreamPlatformListView(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class StreamPlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer