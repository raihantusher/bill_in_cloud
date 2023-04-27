from django.db import models


# Create your models here.

# +------------+    +------------+    +------------+    +------------+
# |   Customer |    |    Service |    |  Subscription  |  |     Bill   |
# +------------+    +------------+    +------------+    +------------+
# |  + id      |    |  + id      |    |  + id        |    |  + id      |
# |  | name    |    |  | name    |    |  | start_date |    |  | amount  |
# |  | address |    |  | price   |    |  | end_date   |    |  | paid    |
# |  | email   |    +------------+    |  + customer_id |   |  | due_date|
# |  +---------+                     |  + service_id  |   +------------+
#                                   +---------------+

class CustomerProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Package(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    service = models.ForeignKey(Package, on_delete=models.CASCADE)


class Bill(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    next_due_date = models.DateTimeField(null=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
