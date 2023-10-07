from django.db import models
from django.contrib.auth.models import User
from shop.models import CartItems


# Create your models here.
class RegistrationData(models.Model):
    name = models.CharField("Name", max_length=100, null=False)
    surname = models.CharField("Surname", max_length=100, null=False)
    phone = models.IntegerField("Phone", null=False)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.CharField("Date of Birth", max_length=10, null=True)
    gender = models.CharField("Gender", max_length=10, null=True)
    propic = models.ImageField(upload_to="userpropic/",
                               null=True,
                               blank=True,
                               default="/default/user-profile.jpg")
    date = models.DateField('Date', auto_now_add=True)

    def __str__(self):
        return self.email.username


class UserAddress(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    house_no = models.CharField("House No",max_length=10, null=True)
    landmark = models.CharField("Landmark", max_length=100, null=True)
    country = models.CharField("Country", max_length=30, null=True)
    state = models.CharField("State", max_length=30, null=True)
    city = models.CharField("City", max_length=30, null=True)
    pincode = models.CharField("Pincode",max_length=10, null=True)

    def __str__(self):
        return self.email.username


class ContactUs(models.Model):
    name = models.CharField("Name", max_length=100, null=False)
    email = models.CharField("Email", max_length=50, null=False)
    subject = models.CharField("Subject", max_length=200, null=False)
    message = models.CharField("Message", max_length=5000, null=False)

    def __str__(self):
        return self.email
