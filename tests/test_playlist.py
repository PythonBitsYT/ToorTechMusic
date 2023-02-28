"""
This module consists of playlist test cases
"""
from tests.db_setup.playlist_db_setup import Playlist_DB_Setup
from playlist.models import Playlist, PlaylistTrack
from rest_framework import status


class Test_Playlist(Playlist_DB_Setup):
    """ Test playlist APIs """

    def setUp(self):
        """ Setup db """
        self._headers = {"content_type": "application/json"}
        return super().setUp()
    

    def test_playlist_listing(self):
        """ Test playlist listing """
        # Case 1: Single Playlist
        response = self.client.get("/data/playlist/", **self._headers)
        _expected_response = [
                                {'playlist_id': self._playlist_1.playlist_id.__str__(), 
                                 'customer': self._playlist_1.customer_id, 
                                 'name': self._playlist_1.name, 
                                 'tracks': list(self._playlist_1.tracks.all().values("id"))}
                             ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), _expected_response)

        # Create another playlist
        self._playlist_2 = Playlist.objects.create(customer=self._customer_2, name="Playlist2")
        self._playlist_2_track_1 = PlaylistTrack.objects.create(playlist=self._playlist_1, track=self._track_1)

        # Case 2: Multiple playlist
        response = self.client.get("/data/playlist/", **self._headers)
        _expected_response = [
                                {'playlist_id': self._playlist_1.playlist_id.__str__(), 
                                 'customer': self._playlist_1.customer_id, 
                                 'name': self._playlist_1.name, 
                                 'tracks': list(self._playlist_1.tracks.all().values("id"))},

                                 {'playlist_id': self._playlist_2.playlist_id.__str__(), 
                                 'customer': self._playlist_2.customer_id, 
                                 'name': self._playlist_2.name, 
                                 'tracks': list(self._playlist_2.tracks.all().values("id"))}
                             ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), _expected_response)


    def test_playlist_create(self):
        """ Test playlist create """
        # Case 1: Initial State - Single Playlist
        self.assertEqual(1, Playlist.objects.count())

        # Create playlist
        _data = {"customer": 1, "name": "Playlist2", "tracks":[{"track":self._track_1.id}]}
        response = self.client.post("/data/playlist/", **self._headers, data=_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Case 2: New playlist added
        self.assertEqual(2, Playlist.objects.count())


    def test_playlist_update(self):
        """ Test playlist update """
        # Case 1: Initial State - Single Playlist
        self.assertEqual(1, Playlist.objects.count())
        self.assertEqual(self._playlist_1.name, "Playlist1")

        # Update playlist
        _data = {"customer": 1, "name": "PlaylistNewName", "tracks":[{"track":self._track_1.id}]}
        response = self.client.put(f"/data/playlist/{self._playlist_1.id}/", **self._headers, data=_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Case 2: Playlist name updated
        self._playlist_1.refresh_from_db()
        self.assertEqual(1, Playlist.objects.count())
        self.assertEqual(self._playlist_1.name, "PlaylistNewName")


    def test_playlist_delete(self):
        """ Test playlist delete """
        # Case 1: Initial State - Single Playlist
        self.assertEqual(1, Playlist.objects.count())
        
        # Delete playlist
        response = self.client.delete(f"/data/playlist/{self._playlist_1.id}/", **self._headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Case 2: Playlist deleted
        self.assertEqual(0, Playlist.objects.count())
    