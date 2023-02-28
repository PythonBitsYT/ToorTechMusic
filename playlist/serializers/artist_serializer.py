"""
This module consists of Artist serialier
"""
from rest_framework import serializers
from playlist.models import Artist



class ArtistSerializer(serializers.ModelSerializer):
    """ Artist model serizlier """
    class Meta:
        model = Artist
        fields = ['name', 'gender']
