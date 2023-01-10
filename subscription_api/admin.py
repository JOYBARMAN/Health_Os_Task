from django.contrib import admin
from .models import SubscriptionPlan,Subscription

class SubscriptionPlanModelAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name','company', 'fee', 'duration')
    list_filter = ('created_at',)
    search_fields = ('name',)
    ordering = ('name','id')
    filter_horizontal = ()

class SubscriptionModelAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('customer','phone_number', 'plan', 'start_date','end_date')
    list_filter = ('start_date',)
    search_fields = ('customer',)
    ordering = ('customer','id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(SubscriptionPlan, SubscriptionPlanModelAdmin)
admin.site.register(Subscription, SubscriptionModelAdmin)
