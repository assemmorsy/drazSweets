from django.db import models

# Create your models here.
class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField( max_length=11 , blank=True)
    address = models.CharField(max_length=200 , blank=True)
    financialAccount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    itemId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    itemCode = models.IntegerField()
    price = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

class RecordInOrder(models.Model):
    recordId = models.AutoField(primary_key=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField() # 0 not yet  ---   1 Done 
    

class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    customer =  models.ForeignKey("Customer", on_delete=models.CASCADE)
    publishedAt = models.DateTimeField(auto_now=True, auto_now_add=False)
    deadLine =  models.DateTimeField(auto_now=False, auto_now_add=False)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2 )
    