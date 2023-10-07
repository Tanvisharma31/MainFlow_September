from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from .models import RegistrationData, ContactUs, UserAddress
from .models import CartItems
from django_project.mail_verication import registration_confirmation_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django_project.tokens import generate_token

# from django.core.mail import send_mail
# import hashlib

from datetime import datetime


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        cart_p_count = CartItems.objects.filter(
            cart__is_paid=False, cart__user=request.user).count()
    else:
        cart_p_count = ""
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = ContactUs(name=name,
                         email=email,
                         subject=subject,
                         message=message)
        data.save()
        return render(request,
                      "index.html",
                      context={"cart_p_count": cart_p_count})
    else:
        return render(request,
                      "index.html",
                      context={"cart_p_count": cart_p_count})


def login(request):
    if request.user.is_authenticated:
        return render(request, "index.html")

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)

        user = auth.authenticate(username=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'invalid credentials')
            return render(request, "mainapp/login.html")
    else:
        return render(request, "mainapp/login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


def header(request):
    return render(request, "header.html")


def registration(request):
    if request.user.is_authenticated:
        return render(request, "index.html")

    if request.method == "GET":
        ref = request.GET.get('ref')
        if ref == None:
            ref = ""

    if request.method == "POST":
        fname = request.POST['name']
        lname = request.POST['surname']
        phone = request.POST['phone']
        username = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username):
            messages.error(
                request, "email already exist! Please try some other email.")
            return redirect('registration')

        if RegistrationData.objects.filter(phone=phone).exists():
            messages.error(request, "Phone number Already Registered!!")
            return redirect('registration')

        if password == confirm_password:
            main_user = User.objects.create_user(username=username,
                                                 email=username,
                                                 password=password)
            main_user.first_name = fname
            main_user.last_name = lname
            main_user.is_active = False       # uncoment this line for user activation mail
            main_user.save()

            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S").split(" ")[0]

            # uncoment below lines for user activation mail

            current_site = get_current_site(request)
            message = render_to_string('mail/email_confirmation.html', {

                'fname': fname,
                'lname': lname,
                'username': username,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(main_user.pk)),
                'token': generate_token.make_token(main_user)
            })

            ismailsent = registration_confirmation_mail(user_email=username, message=message)
            if ismailsent:
                user1 = RegistrationData(name=fname,
                                        surname=lname,
                                        phone=phone,
                                        email=main_user,
                                        date=date)
                user1.save()
                # return redirect('/login')  # coment this line for user activation mail

                
                return render(request, "mail/account_confirmation_mail.html")
            else:
                main_user.delete()
                print("Mail not sent")
                return render(request, "mainapp/registration.html")

        else:
            form_data = {
                "name": fname,
                "surname": lname,
                "username": username,
                "email": username,
                "password": "",
                "confirm_password": ""
            }
            messages.error(
                request,
                "The password and confirmation password do not match.")
            return render(request, "mainapp/registration.html", form_data)

    else:
        return render(request, "mainapp/registration.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        auth.login(request, myuser)

        messages.success(request, "Your Account has been activated !")

        return redirect('login')
    else:
        return render(request, 'mail/activation_failed.html')


def aboutus(request):
    return render(request, 'mainapp/aboutus.html')


def contactus(request):
    return render(request, 'mainapp/aboutus.html')


def profile(request):
    if request.user.is_authenticated:
        username = request.user
        userdata = RegistrationData.objects.get(email=username)
        address,_ = UserAddress.objects.get_or_create(email=request.user)
        if request.method == "POST":
            try:
                print("User info Post method")
                fname = request.POST['fname']
                if len(fname)>1:
                    userdata.fname = fname
                lname = request.POST['lname']
                if len(lname)>1:
                    userdata.lname = lname
                dob = request.POST['dob']
                if len(dob)>1:
                    userdata.dob = dob
                gender = request.POST['gender']
                if len(gender)>1:
                    userdata.gender = gender
                userdata.save()
            except:
                try:
                    print("address post method")
                    house = request.POST['house']
                    if len(house)>1:
                        address.house_no = house
                    locality = request.POST['locality']
                    if len(locality)>1:
                        address.landmark = locality
                    city = request.POST['city']
                    if len(city)>1:
                        address.city = city
                    state = request.POST['state']
                    if len(state)>1:
                        address.state = state
                    pincode = request.POST['pincode']
                    if len(pincode)>1:
                        address.pincode = pincode
                    country = request.POST['country']
                    if len(country)>1:
                        address.country = country
                    address.save()

                except:
                    propic = request.FILES['propic']
                    userdata.propic = propic
                    userdata.save()

        print(username)
        return render(request, "profilepage.html", context={"userdata": userdata, "address" : address})

    else:
        return redirect("/login")
