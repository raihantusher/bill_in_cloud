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
    date = models.DateField(auto_now_add=True)
    dr = models.FloatField(default=0)
    cr = models.FloatField(default=0)

#model for expenses list
class ExpensesList(models.Model):
    expense_category = models.CharField(max_length=100)
    amount_of_money = models.DecimalField(max_digits=10, decimal_places=2)
    entry_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.expense_category