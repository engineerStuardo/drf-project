from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import MovieList, MovieDetail

urlpatterns = [
    path('list/', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]