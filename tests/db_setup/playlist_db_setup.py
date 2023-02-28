"""
This module consists of DB setup for playlist
"""
from playlist.models import Artist, Album, Track, Playlist, PlaylistTrack
from tests.db_setup.customer_db_setup import Customer_DB_Setup
from django.test import TestCase



class Artist_DB_Setup(TestCase):
    """ Artist Db setup """

    def setUp(self):
        """ Setup artist db """
        super().setUp()
        self._artist_1 = Artist.objects.create(name="Artist1", gender="M")
        self._artist_2 = Artist.objects.create(name="Artist2", gender="F")


class Album_DB_Setup(Artist_DB_Setup):
    """ Album Db setup """

    def setUp(self):
        """ Setup album db """
        super().setUp()
        self._album_1 = Album.objects.create(name="Album1")
        self._album_1.artists.add(self._artist_1)
        self._album_2 = Album.objects.create(name="Album2")
        self._album_2.artists.add(self._artist_1)
        self._album_2.artists.add(self._artist_2)
    

class Track_DB_Setup(Album_DB_Setup):
    """ Track Db setup """

    def setUp(self):
        """ Setup track db """
        super().setUp()
        self._track_1 = Track.objects.create(title="Track1", album=self._album_1)
        self._track_1.artists.add(self._artist_1)

        self._track_2 = Track.objects.create(title="Track2", album=self._album_2)
        self._track_2.artists.add(self._artist_1)
        self._track_2.artists.add(self._artist_2)

        self._track_3 = Track.objects.create(title="Track2")
        self._track_3.artists.add(self._artist_1)


class Playlist_DB_Setup(Track_DB_Setup, Customer_DB_Setup):
    """ Playlist Db setup """

    def setUp(self):
        """ Setup playlist db """
        super().setUp()
        self._playlist_1 = Playlist.objects.create(customer=self._customer_1, name="Playlist1")
        self._playlist_1_track_1 = PlaylistTrack.objects.create(playlist=self._playlist_1, track=self._track_1)
        self._playlist_1_track_2 = PlaylistTrack.objects.create(playlist=self._playlist_1, track=self._track_2)
    