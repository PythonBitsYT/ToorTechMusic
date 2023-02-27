"""
This module consists of models for playlist
"""
from django.db import models
from playlist.models.track import Track
from customers.models import Customer
import uuid



class Playlist(models.Model):
    """ Model for playlist """ 
    playlist_id = models.UUIDField(default=uuid.uuid4)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tracks = models.ManyToManyField(Track, through="PlaylistTrack", related_name="playlist_tracks")

    # Update fields
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """ Dunder method to return human redable name """
        return f"Playlist [{self.id} - {self.name}]"
    

class PlaylistTrack(models.Model):
    """ Model for Playlist tracks """
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    priority = models.IntegerField(blank=True)

    class Meta:
        ordering = ['priority']

    def save(self, *args, **kwargs):
        """ Override default save method """
        _max_track_count = PlaylistTrack.objects.filter(playlist=self.playlist).count()
        self.priority = _max_track_count + 1
        super(PlaylistTrack, self).save(*args, **kwargs)
    