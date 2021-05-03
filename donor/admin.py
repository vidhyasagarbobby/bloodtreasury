from django.contrib import admin
from donor.models import Donor, DonationHistory

class DonorAdmin(admin.ModelAdmin):
    pass

class DonationHistoryAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Donor, DonorAdmin)
admin.site.register(DonationHistory, DonationHistoryAdmin)