from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20 )
    order_status = serializers.HiddenField(default = "PENDING")
    quantity = serializers.IntegerField()
  


    class Meta:
        model = Order
        fields = ['size', 'order_status', 'quantity']




class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['size', 'order_status', 'quantity','created_at','updated_at']

class UserOrderDetailSerializer(serializers.ModelSerializer):
    # owner = serializers.CharField(source="customer", read_only=True) #To get a username of the customer 
    class Meta:
        model = Order
        fields = ['customer','id','size', 'order_status', 'quantity','created_at','updated_at']
