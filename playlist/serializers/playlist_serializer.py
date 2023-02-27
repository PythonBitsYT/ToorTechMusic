"""
This module consists of Playlist serialier
"""
from rest_framework import serializers
from playlist.models import Playlist, PlaylistTrack, Track



class PlayListTrackSerializer(serializers.ModelSerializer):
    """ Platlist track model serizlier """
    class Meta:
        model = PlaylistTrack
        fields = ['id', 'playlist', 'track', 'priority']
        extra_kwargs = {'playlist': {'required': False}, 'track': {'required': False}}


class PlayListSerializer(serializers.ModelSerializer):
    """ Model serializer """
    tracks = PlayListTrackSerializer(many=True, required=False)
    class Meta:
        model = Playlist
        fields = ['playlist_id', 'customer', 'name', 'tracks']
    
    def update(self, instance, validated_data):
        track_data = validated_data.pop('tracks')
        instance = super(PlayListSerializer,self).update(instance, validated_data)
        instance.playlisttrack_set.all().delete()
        for track in track_data:
            PlaylistTrack.objects.create(playlist=instance, track=track["track"])
        return instance
