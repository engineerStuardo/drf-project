from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='watch_list_detail', lookup_field='pk')
    platform = serializers.HyperlinkedRelatedField(
        view_name='stream_platform_detail',
        read_only=True,
        lookup_field='pk'
    )

    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='stream_platform_detail', lookup_field='pk')
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'