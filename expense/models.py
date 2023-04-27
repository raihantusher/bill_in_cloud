from django.db import models


# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=35)


class Category(models.Model):
    name = models.CharField(max_length=35)


class Transaction(models.Model):
    title = models.CharField(max_length=200)
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL)
    cat = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.CharField()
    dr = models.FloatField(default=0)
    cr = models.FloatField(default=0)
