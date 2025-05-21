from django.urls import path, include
from watchlist_app.api.views import (WatchListView, WatchListDetailView,
                                     StreamPlatformListView, StreamPlatformDetailView,
                                     ReviewList, ReviewDetail, ReviewCreate)

urlpatterns = [
    # Watch APIS
    path('list/', WatchListView.as_view(), name='watch_list'),
    path('<int:pk>/', WatchListDetailView.as_view(), name='watch_list_detail'),

    # Platform APIS
    path('stream/', StreamPlatformListView.as_view(), name='stream_platform_list'),
    path('stream/<int:pk>/', StreamPlatformDetailView.as_view(), name='stream_platform_detail'),

    # Review APIS
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review_list'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review_create'),
]