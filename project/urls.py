from django.contrib import admin
from django.urls import path
from OrdersApp.views import orderDetails,orders
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',orders,name = "orders"),
    path('order/',orders),
    path('order/<int:id>',orderDetails,name="orderDetails")
]
