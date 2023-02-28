"""
This model consists of views for Customer
"""
from customers.models import Customer
from rest_framework import viewsets
from customers.serializers.customer_serializer import CustomerSerializer



class CustomerViewSet(viewsets.ModelViewSet):
    """ Customer model view set """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
