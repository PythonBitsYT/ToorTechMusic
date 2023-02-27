"""
This module consists of models for customer
"""
from django.db import models
from common.model_enums import Gender
from datetime import date




class Customer(models.Model):
    """ Model for customers """
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.FEMALE)

    # Update fields
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    @property
    def _age(self):
        """ Identify the age of a customer from the dob """ 
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def __str__(self):
        """ Dunder method to return human redable name """
        return f"Customer [{self.id} - {self.name}]"
