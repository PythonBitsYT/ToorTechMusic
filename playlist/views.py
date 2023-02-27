"""
This model consists of views for playlist
"""
from playlist.models import Playlist
from rest_framework import viewsets
from playlist.serializers.playlist_serializer import PlayListSerializer



class PlayListViewSet(viewsets.ModelViewSet):
    """ Playlist model view set """
    serializer_class = PlayListSerializer
    queryset = Playlist.objects.all()
