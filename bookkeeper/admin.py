from django.contrib import admin

# Register your models here.
from .models import Category, Journal, Transaction


admin.site.register(Category)
admin.site.register(Journal)
admin.site.register(Transaction)
