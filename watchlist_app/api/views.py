from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from watchlist_app.models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer


class WatchListView(APIView):


    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailView(APIView):


    def get_object(self, pk):
        try:
            return WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return None


    def get(self, request, pk):
        movie = self.get_object(pk)

        if not movie:
            return Response({"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        movie = self.get_object(pk)

        if not movie:
            return Response({"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        movie = self.get_object(pk)

        if not movie:
            return Response({"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response({"message": "Movie deleted successfully!", "status": "204"},status=status.HTTP_204_NO_CONTENT)


class StreamPlatformListView(APIView):


    def get(self, request):
        stream_platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stream_platforms, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailView(APIView):


    def get_object(self, pk):
        try:
            return StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return None


    def get(self, request, pk):
        stream_platform = self.get_object(pk)
        if not stream_platform:
            return Response({"message": "Stream platform not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(stream_platform, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        stream_platform = self.get_object(pk)
        if not stream_platform:
            return Response({"message": "Stream platform not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        stream_platform = self.get_object(pk)
        if not stream_platform:
            return Response({"message": "Stream platform not found"}, status=status.HTTP_404_NOT_FOUND)
        stream_platform.delete()
        return Response({"message": "Stream platform deleted successfully!", "status": "204"}, status=status.HTTP_204_NO_CONTENT)