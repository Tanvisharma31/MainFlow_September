from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from shop.models import ProductDetails, Cart, CartItems
from django_project.payment import order, verify_payment_request
from .models import Order, OrderItems


# Create your views here.
def checkout(request):
    if request.user.is_authenticated:
        action = request.GET.get('action')
        current_order = None
        payment = None
        discount = 0
        shiping = 0
        total_amount = []
        cart = CartItems.objects.filter(cart__is_paid=False,
                                        cart__user=request.user)
        cart_p_count = cart.count()

        for item in cart:
            product_amount = item.product.price
            product_count = item.count
            total_amount.append(product_amount * product_count)

        if action == "pay":
            username = request.user.username
            email = request.user.email
            fname = request.user.first_name
            lname = request.user.last_name
            total_amount = sum(total_amount) - discount

            current_order = order(username=username,
                                  email=email,
                                  fname=fname,
                                  lname=lname,
                                  amount_rs=total_amount)

            order_data = Order()
            order_data.user = request.user
            order_data.order_id = current_order['id']
            order_data.save()

            for item in cart:
                items = OrderItems()
                items.order = Order.objects.get(user=request.user,
                                                order_id=current_order['id'])
                items.product = item.product
                items.count = item.count
                items.save()

            ordered_cart = Cart.objects.get(user=request.user)
            ordered_cart.delete()

            current_site_domain = get_current_site(request).domain

            return render(request,
                          "shop/cart.html",
                          context={
                              "order": current_order,
                              "payment": order_data,
                              "name": f"{fname} {lname}",
                              "domain": current_site_domain
                          })
        else:
            print(order)
            return render(request,
                          "courses/enroll.html",
                          context={
                              "course": course,
                              "order": current_order
                          })
    else:
        return redirect("login")


# <QueryDict: {'razorpay_payment_id': ['pay_JqmguXq3XyZ21p'], 'razorpay_order_id': ['order_JqmghXkLr7mwfI'], 'razorpay_signature': ['3b1113b41e94e568920478d9d1c2a30838ec91d8bab2d106d9ed22bd3ef3390c']}>
@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        data = request.POST
        # try:
        verify_payment_request(data)
        razorpay_order_id = data['razorpay_order_id']
        razorpay_payment_id = data['razorpay_payment_id']
        payment = Order.objects.get(order_id=razorpay_order_id)
        payment.payment_id = razorpay_payment_id
        payment.status = True
        payment.save()

        print("Your order is done .......... ")
        return redirect("/")
        # except:
        # return HttpResponse("Invalid payment details")
