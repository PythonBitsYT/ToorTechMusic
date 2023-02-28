"""
This module consists of Customer serialier
"""
from rest_framework import serializers
from customers.models import Customer



class CustomerSerializer(serializers.ModelSerializer):
    """ Customer model serizlier """
    class Meta:
        model = Customer
        fields = ['name', 'dob', 'gender']
