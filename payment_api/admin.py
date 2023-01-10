from django.contrib import admin
from .models import Payment

class PaymentModelAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('customer','amount', 'method', 'subscription')
    list_filter = ('created_at',)
    search_fields = ('customer',)
    ordering = ('customer','id')
    filter_horizontal = ()

admin.site.register(Payment, PaymentModelAdmin)