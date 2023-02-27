"""
This module consists of models for album
"""
from django.db import models
from playlist.models.artist import Artist



class Album(models.Model):
    """ Model for music album """ 
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist)

    # Update fields
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """ Dunder method to return human redable name """
        return f"Album [{self.id} - {self.name}]"
    