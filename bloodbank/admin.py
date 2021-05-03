from django.contrib import admin
from bloodbank.models import BloodBank, BloodStock

class BloodBankAdmin(admin.ModelAdmin):
    pass

class BloodStockAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(BloodBank, BloodBankAdmin)
admin.site.register(BloodStock, BloodStockAdmin)
