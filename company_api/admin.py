from django.contrib import admin
from .models import Company

class CompanyModelAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name','address', 'website', 'industry')
    list_filter = ('created_at',)
    search_fields = ('name',)
    ordering = ('name','id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(Company, CompanyModelAdmin)
