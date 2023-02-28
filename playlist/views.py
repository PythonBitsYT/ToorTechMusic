"""
This model consists of views for playlist
"""
from playlist.models import Playlist, Artist, Album, Track
from rest_framework import viewsets
from playlist.serializers.playlist_serializer import PlayListSerializer
from playlist.serializers.artist_serializer import ArtistSerializer
from playlist.serializers.album_serializer import AlbumSerializer
from playlist.serializers.track_serializer import TrackSerializer



class PlayListViewSet(viewsets.ModelViewSet):
    """ Playlist model view set """
    serializer_class = PlayListSerializer
    queryset = Playlist.objects.all()


class ArtistViewSet(viewsets.ModelViewSet):
    """ Artist model view set """
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class AlbumViewSet(viewsets.ModelViewSet):
    """ Album model view set """
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class TrackViewSet(viewsets.ModelViewSet):
    """ Track model view set """
    serializer_class = TrackSerializer
    queryset = Track.objects.all()

