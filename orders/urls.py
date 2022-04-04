
from django.contrib import admin
from django.urls import path
from .views import order_view,createOrder_view, orderDetail_view,userOrder_view,userDetailOrderDetail_view
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('orders/',order_view, name="orders"),
    path('orders/user/<int:user_id>/create/',createOrder_view, name="create-order"),
    path('orders/<int:order_id>/',orderDetail_view, name="orderDetail"),
    path('user/<int:user_id>/orders/',userOrder_view, name="userOrderDetail"),
    path('user/<int:user_id>/order/<int:order_id>/',userDetailOrderDetail_view),

]
