from django.contrib import admin

# Register your models here.
from .models import CustomerProfile, Package, Subscription, Bill

admin.site.register(CustomerProfile)
admin.site.register(Package)
admin.site.register(Subscription)
admin.site.register(Bill)