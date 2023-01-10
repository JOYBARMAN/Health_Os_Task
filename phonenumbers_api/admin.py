from django.contrib import admin
from .models import PhoneNumbers

class PhoneNumberModelAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('customer','company', 'phone_number')
    list_filter = ('created_at',)
    search_fields = ('customer',)
    ordering = ('customer','id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(PhoneNumbers, PhoneNumberModelAdmin)