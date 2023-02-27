"""
This module consists of models for music track
"""
from django.db import models
from playlist.models.album import Album
from playlist.models.artist import Artist



class Track(models.Model):
    """ Model for music track """ 
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    artists = models.ManyToManyField(Artist)

    # Update fields
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        """ Dunder method to return human redable name """
        return f"Track/Song [{self.id} - {self.title}]"