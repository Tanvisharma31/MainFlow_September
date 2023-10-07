from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class ProductDetails(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField("Name", max_length=100, null=False)
    brand = models.CharField("Brand", max_length=100, null=False)
    category = models.CharField("Category", max_length=100, null=False)
    description = models.CharField("Description", max_length=1000, null=False, default="")
    keywords = models.CharField("Key Words", max_length=100, null=False)
    image1 = models.ImageField(upload_to="products/images")
    image2 = models.ImageField(upload_to="products/images")
    image3 = models.ImageField(upload_to="products/images")
    image4 = models.ImageField(upload_to="products/images")
    status = models.BooleanField(default=False)
    price = models.IntegerField("Price", null=False)
    date = models.DateField('Date', auto_now_add=True)

    def __str__(self):
        return self.brand


class Cart(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    count = models.IntegerField("Count", default=1)

class WishList(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)

class WishListItems(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
