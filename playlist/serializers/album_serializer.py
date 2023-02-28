"""
This module consists of Album serialier
"""
from rest_framework import serializers
from playlist.serializers.artist_serializer import ArtistSerializer
from playlist.models import Album



class AlbumSerializer(serializers.ModelSerializer):
    """ Album model serizlier """
    artists = ArtistSerializer(many=True, required=False)
    class Meta:
        model = Album
        fields = ['name', 'artists']
