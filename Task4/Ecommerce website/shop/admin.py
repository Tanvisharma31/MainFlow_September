from django.contrib import admin
from .models import ProductDetails, Cart, CartItems, WishList, WishListItems

# Register your models here.

admin.site.register(ProductDetails)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(WishList)
admin.site.register(WishListItems)
