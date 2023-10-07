from django.db import models
from django.contrib.auth.models import User
from shop.models import ProductDetails

# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length = 50 , null = False)
    payment_id = models.CharField(max_length = 50)
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    time = models.TimeField("Time", auto_now_add=True)
    date = models.DateTimeField("Date", auto_now_add=True)
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.order_id

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    count = models.IntegerField("Count", default=1)

    def __str__(self):
        return self.order.order_id

