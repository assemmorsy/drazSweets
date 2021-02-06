from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer , Item , Order,RecordInOrder

# Create your views here.
def orderDetails(req, id) :
    order = Order.objects.get(orderId = id)
    customer = Customer.objects.get(customerId = order.customer.customerId)
    itemsInOrder = RecordInOrder.objects.filter(order = id)
    
    context = {'order' : order  , 'customer' :customer , 'itemsInOrder' : itemsInOrder }
    return render(req , 'orderDetails.html', context=context)

def orders(req):
    allOrders = Order.objects.all()
    orders = []
    for order in allOrders :
        itemsInOrder = RecordInOrder.objects.filter(order = order.orderId) 
        itemNames = []
        for item in itemsInOrder : 
            if item.item.name not in itemNames : 
                itemNames.append(item.item.name)
        orders.append({
            'orderId' : order.orderId ,
            'customerName' : Customer.objects.get(customerId = order.customer.customerId).name,
            'orderDeadLine' :order.deadLine,
            'itemNames' :itemNames
            })

    context = {'orders' : orders}
    #print(orders)
    return render(req , 'orders.html', context=context)
