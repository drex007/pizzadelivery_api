from pyexpat import model
from django.contrib import admin

# Register your models here.
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
     list_display = ['size', 'order_status', 'quantity', 'created_at']
