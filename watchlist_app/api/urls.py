from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import (WatchListView, WatchListDetailView,
                                     ReviewList, ReviewDetail, ReviewCreate,
                                     StreamPlatformViewSet)


router = DefaultRouter()
router.register(r'stream', StreamPlatformViewSet, basename='stream_platform')


urlpatterns = [
    # Watch APIS
    path('list/', WatchListView.as_view(), name='watch_list'),
    path('<int:pk>/', WatchListDetailView.as_view(), name='watch_list_detail'),

    # Platform APIS:
    # Including this url in the root urlpatterns
    # /watch/stream/
    # /watch/stream/<pk>/
    path('', include(router.urls)),

    # Review APIS
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review_list'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review_create'),
]