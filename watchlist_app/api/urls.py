from django.urls import path, include
from watchlist_app.api.views import (WatchListView, WatchListDetailView,
                                     StreamPlatformListView, StreamPlatformDetailView,
                                     ReviewList, ReviewDetail)

urlpatterns = [
    path('list/', WatchListView.as_view(), name='watch_list'),
    path('<int:pk>/', WatchListDetailView.as_view(), name='watch_list_detail'),
    path('stream/', StreamPlatformListView.as_view(), name='stream_platform_list'),
    path('stream/<int:pk>/', StreamPlatformDetailView.as_view(), name='stream_platform_detail'),
    path('review/', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
]