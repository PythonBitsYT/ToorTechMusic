"""
This module consists of Track serialier
"""
from playlist.serializers.artist_serializer import ArtistSerializer
from playlist.serializers.album_serializer import AlbumSerializer
from rest_framework import serializers
from playlist.models import Track, Album



class TrackSerializer(serializers.ModelSerializer):
    """ Track model serizlier """
    artists = ArtistSerializer(many=True, required=False)
    album = AlbumSerializer(required=False, read_only=True)
    class Meta:
        model = Track
        fields = ['title', 'album', 'artists']
