"""
This module consists of models for artist
"""
from django.db import models
from common.model_enums import Gender


class Artist(models.Model):
    """ Model for artist """
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.FEMALE)

    # Update fields
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """ Dunder method to return human redable name """
        return f"Artist [{self.id} - {self.name}]"
