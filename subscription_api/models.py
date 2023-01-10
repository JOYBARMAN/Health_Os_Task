from django.db import models
from company_api.models import Company
from customer_accounts_api.models import Customer
from phonenumbers_api.models import PhoneNumbers

duration_choise = (
    ("Monthly","Monthly"),
    ("Yearly","Yearly")
)

# distinct Plans model
class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100,choices=duration_choise)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + str(self.fee)

# model for subscription
class Subscription(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone_number = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    cancel_subscripton = models.BooleanField(default=False)
    is_pay = models.BooleanField(default=False)


    def __str__(self):
        return self.customer.name +" "+str(self.plan.name)
