from django.contrib import admin

# Register your models here.
from .models import VolunteerRegistrationModel


class VolunteerRegistrationModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'loginid',
        'password',
        'mobile',
        'email',
        'status'

    )


admin.site.register(VolunteerRegistrationModel,
                    VolunteerRegistrationModelAdmin)
