from django.contrib import admin
from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """ Register Customer admin """
    list_display = ['id', 'name', 'gender', 'created_at', 'updated_at']
    search_fields = ['id', 'name']
