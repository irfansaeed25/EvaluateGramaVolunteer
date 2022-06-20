from django.contrib import admin
from .models import FamilyMember, Services, VolunteerRating


# Register your models here.


class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'dob',
        'mobileNo',
        'aadharNo',
        'rationNo',
        'pan',
        'address',
        'wardNo',
        'volunteer',
    )


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'mobileNo',
        'aadharNo',
        'name',
        'serviceSelected',
        'requiredDocuments',
        'status'
    )


class VolunteerRatingAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'volunteer',
        'rating',
    )


admin.site.register(FamilyMember, FamilyMemberAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(VolunteerRating, VolunteerRatingAdmin)
