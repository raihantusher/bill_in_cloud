from django.db import models
from datetime import datetime, timedelta

current_date = datetime.now()

# Get the first day of the current year
first_day_of_year = datetime(current_date.year, 1, 1)

# Get the first day of the next year
first_day_of_next_year = datetime(current_date.year + 1, 1, 1)

# Subtract one day to get the last day of the current year
last_day_of_year = first_day_of_next_year - timedelta(days=1)


class Category(models.Model):
    ACCOUNTS = (
        ('asset_expense', 'Asset/Expense'),  # inc = debit dec = credit
        ('liabilities_equity', 'Liabilities/Income/Capital'),  # dec = debit inc = credit
    )
    name = models.CharField(max_length=35)
    color_code = models.CharField(max_length=13, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=120, choices=ACCOUNTS, default="asset_expense")
    clas = models.CharField(max_length=100, null=True, blank=True)
    default_account = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}    -> {self.clas}"


class Journal(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Create your models here.
class TransactionManager(models.Manager):
    def calculate_net_balance(self, category, start_date=first_day_of_year, end_date=last_day_of_year):
        obj = self.filter(category__name=category).first()
        print(obj)
        total_debit = self.filter(category__name=category, date__range=(start_date, end_date)).aggregate(
            total_debit=models.Sum('debit'))[
                          'total_debit'] or 0
        total_credit = self.filter(category__name=category, date__range=(start_date, end_date)).aggregate(
            total_credit=models.Sum('credit'))[
                           'total_credit'] or 0
        # print(obj.category.account_type)
        try:
            if obj.category.account_type == "asset_expense":
                print(total_debit)
                return total_debit - total_credit
            else:
                print(total_debit)
                return total_credit - total_debit
        except:
            return 0


class Transaction(models.Model):
    TYPES = (
        ('credit', 'Credit'),  # inc = debit dec = credit
        ('debit', 'Debit'),  # dec = debit inc = credit
    )
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=120, choices=TYPES, default="credit")
    objects = TransactionManager()

    def __str__(self):
        return f"Account: {self.category} -- {self.journal} -Debit: {self.debit} - Credit {self.credit} - {self.date}"
