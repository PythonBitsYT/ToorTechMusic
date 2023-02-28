"""
This module consists of DB setup for customer
"""
from customers.models import Customer
from django.test import TestCase
from datetime import datetime



class Customer_DB_Setup(TestCase):
    """ Customer Db setup """

    def setUp(self):
        """ Setup customer db """
        self._customer_1 = Customer.objects.create(name="Customer1", dob=datetime(year=2000, month=10, day=10), gender="M")
        self._customer_2 = Customer.objects.create(name="Customer2", dob=datetime(year=2001, month=10, day=10), gender="F")
        self._customer_3 = Customer.objects.create(name="Customer3", dob=datetime(year=2002, month=10, day=10), gender="F")
    