from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import ProductDetails, Cart, CartItems, WishList, WishListItems
import json



def products(request):
    if request.user.is_authenticated:
        cart_p_count = CartItems.objects.filter(
            
            cart__is_paid=False, cart__user=request.user).count()
    else:
        cart_p_count = ""

    products = ProductDetails.objects.all()
    wishlistproduct = []
    if request.user.is_authenticated:
        # wishlist = WishList.objects.get_or_create(user = request.user)
        wishlist_product = WishListItems.objects.filter(
            
            wishlist__user=request.user)
        for product in wishlist_product:
            wishlistproduct.append(product.product)

    return render(request,
                 
                  "shop/products.html",
                 
                  context={
                      
                      "products": products,
                     
                      "wishlistproduct": wishlistproduct,
                     
                      "cart_p_count":  cart_p_count
                  
                  })



def tracker(request):
    return render(request, "shop/products.html")



def search(request):
    return render(request, "shop/products.html")



def addproduct(request):
    if request.method == "GET":
        ref = request.GET.get('ref')
        if ref == None:
            ref = ""

    if request.method == "POST":
        name = request.POST.get('productName')
        brand_name = request.POST.get('productCompany')
        category = request.POST.get('productCategory')
        description = request.POST.get('description')
        keywords = request.POST.get('keywords')
        image1 = request.FILES.get('image1', None)
        image2 = request.FILES.get('image2', None)
        image3 = request.FILES.get('image3', None)
        image4 = request.FILES.get('image4', None)
        status = request.POST.get('availability')
        price = request.POST.get('price')

        if status != "in_stock":
            status = False
        else:
            status = True

        product = ProductDetails(product_name=name,
                                
                                 brand=brand_name,
                                
                                 category=category,
                                 description=description,
                                
                                 keywords=keywords,
                                
                                 image1=image1,
                                 image2=image2,
                                
                                 image3=image3,
                                
                                 image4=image4,
                                 
                                 status=status,
                                
                                 price=price)
        product.save()
        messages.success(request, "your product is added successfully")

    return render(request, "shop/addproduct.html")


def viewProduct(request, product_id):
    product = ProductDetails.objects.get(product_id=product_id)
    if request.user.is_authenticated:
        cart_p_count = CartItems.objects.filter(
            
            cart__is_paid=False, cart__user=request.user).count()
    else:
        cart_p_count = ""

    context = {"product": product, "cart_p_count": cart_p_count}
    return render(request, "shop/product_page.html", context=context)



def cart(request):
    if request.user.is_authenticated:
        username = request.user
        total_amount = []
        cart, _ = Cart.objects.get_or_create(user=request.user, is_paid=False)
        cart = CartItems.objects.filter(cart__is_paid=False,
                                       
                                        cart__user=request.user)
        cart_p_count = cart.count()
        for item in cart:
            product_amount = item.product.price
            product_count = item.count
            total_amount.append(product_amount * product_count)
        total_amount = sum(total_amount)

        context = {
            
            "cart_items": cart,
           
            "cart_p_count": cart_p_count,
           
            "total_amount": total_amount
        
        }
        return render(request, "shop/cart.html", context=context)

    else:
        return redirect("/login")



def add_to_cart(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "GET":
            try:
                p_id = request.GET.get('pid')
                product = ProductDetails.objects.get(product_id=p_id)
                cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

                if CartItems.objects.filter(cart=cart,
                                           
                                            product=product).exists():
                    print("Product Exist")
                    messages.success(request,
                                    
                                     "Product already exist in your cart")
                    return HttpResponseRedirect(
                        
                        request.META.get('HTTP_REFERER'))
                else:
                    cart_item = CartItems(cart=cart, product=product)
                    cart_item.save()
                    messages.success(request, "Product added in your cart")
                    return HttpResponseRedirect(
                        
                        request.META.get('HTTP_REFERER'))
            except:
                print("some error")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        return redirect("/login")



def count(request, product_id, ar):
    user = request.user
    product = ProductDetails.objects.get(product_id=product_id)
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    item = CartItems.objects.get(cart=cart, product=product)

    if ar == "add":
        item.count += 1
        item.save()
    elif ar == "remove":
        if item.count >  1:
            item.count -= 1
            item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def remove_from_cart(request, product_id):
    user = request.user
    product = ProductDetails.objects.get(product_id=product_id)
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    item = CartItems.objects.get(cart=cart, product=product)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_to_wishlist(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "GET":
            p_id = request.GET.get('pid')
            product = ProductDetails.objects.get(product_id=p_id)
            wishlist, _ = WishList.objects.get_or_create(user=user)

            wishlistproduct = WishListItems.objects.filter(wishlist=wishlist,
                                                          
                                                           product=product)
            if wishlistproduct.exists():
                wishlistproduct.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                cart_item = WishListItems(wishlist=wishlist, product=product)
                cart_item.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        return redirect("/login")

