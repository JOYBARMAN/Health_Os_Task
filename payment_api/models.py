from django.db import models
from customer_accounts_api.models import Customer
from subscription_api.models import Subscription

# Create your models here.
# model for payment subscription
class Payment(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.customer.name) +" "+str(self.amount)