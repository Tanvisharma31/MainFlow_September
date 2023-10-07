from django.contrib import admin
from .models import RegistrationData, UserAddress, ContactUs

# Register your models here.

admin.site.register(RegistrationData)
admin.site.register(UserAddress)
admin.site.register(ContactUs)