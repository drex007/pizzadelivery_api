from cgitb import lookup
from xmlrpc.client import ResponseError
from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import OrderDetailSerializer, OrderSerializer, UserOrderDetailSerializer
from .models import Order
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
User = get_user_model()


class OrderView(generics.GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    def get(self, request):
        queryset = Order.objects.all()
        serializer= self.serializer_class(instance=queryset, many=True)
        return Response(data= serializer.data, status=status.HTTP_200_OK)



order_view = OrderView.as_view()

class OrderListCreateView(generics.GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        orders = Order.objects.all()
        
        serializer = self.serializer_class(instance= orders,many=True)
        
        return Response(data=serializer.data, status= status.HTTP_201_CREATED)

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
       
        data =request.data
        serilaizer = self.serializer_class(data=data)
        if serilaizer.is_valid():
            serilaizer.save(customer= user)
            return  Response(data=serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(data=serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
        



createOrder_view = OrderListCreateView.as_view()

class OrderDetailView(generics.GenericAPIView):#Better to user Retreieve Api View with lookup_field
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = OrderDetailSerializer
    def get(self, request, order_id):
        order = get_object_or_404(Order,pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        

    def put(self, request, order_id): #You can also user UpdateViewHere 
        data = request.data
        order = get_object_or_404(Order,pk=order_id)
        serializer = self.serializer_class(data=data, instance=order)
        if serializer.is_valid():
            serializer.save(customer=User.objects.get(id=1))
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        
        pass
    
    def delete(self, request, order_id):
        order = get_object_or_404(Order,pk=order_id)
        order.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        

orderDetail_view = OrderDetailView.as_view()


class UserOrderView(generics.GenericAPIView):
    serializer_class= UserOrderDetailSerializer
    queryset = Order.objects.all()
    def get(self, request, user_id):
        queryset= Order.objects.all()
        user = get_object_or_404(User, pk=user_id)
        order = queryset.filter(customer=user)
        serializer = self.serializer_class(instance=order, many=True)
       
        return Response(data=serializer.data ,status=status.HTTP_202_ACCEPTED)
    
      
userOrder_view = UserOrderView.as_view()


class UserDetailOrderDetailView(generics.GenericAPIView): #Getting a partivular Order from a User 
    serializer_class= OrderDetailSerializer
    queryset= Order.objects.all()
    def get(self, request, user_id, order_id):
        queryset= Order.objects.all()
        user = get_object_or_404(User, pk=user_id)
        order = queryset.filter(customer=user).get(id=order_id)
        if order:
            serializer = self.serializer_class(instance=order, many=False)
            return Response(data=serializer.data ,status=status.HTTP_202_ACCEPTED)
        return Response({
            'Search': 'Not Found ' 
        })
    
      
userDetailOrderDetail_view = UserDetailOrderDetailView.as_view()