from django.db import models
from customer_accounts_api.models import Customer
from company_api.models import Company
from phonenumber_field.modelfields import PhoneNumberField

# a customer have several phone number per company
class PhoneNumbers(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name="Phone",unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer.name +" "+str(self.phone_number)
